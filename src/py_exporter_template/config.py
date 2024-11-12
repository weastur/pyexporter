import ssl
import typing
from ipaddress import IPv4Address

from pydantic import (
    BaseModel,
    Field,
    FilePath,
    PositiveInt,
    model_validator,
)
from pydantic.json_schema import SkipJsonSchema
from pydantic.types import DirectoryPath, NewPath
from pydantic_settings import (
    BaseSettings,
    CliSubCommand,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    YamlConfigSettingsSource,
)


class JSONSchema(BaseModel):
    """Dump the JSON schema to a file."""

    path: NewPath = Field(
        default="config.schema.json", description="Path to the schema file"
    )


class Log(BaseModel):
    level: typing.Literal[
        "trace", "debug", "info", "success", "warning", "error", "critical"
    ] = Field(default="info", description="Log level")


class DefaultCollectors(BaseModel):
    gc: bool = Field(default=True, description="Enable the GC collector")
    platform: bool = Field(
        default=True, description="Enable the platform collector"
    )
    process: bool = Field(
        default=True, description="Enable the process collector"
    )


class Collectors(BaseModel):
    disable_created_series: bool = Field(
        default=False, description="Disable created series"
    )
    default: DefaultCollectors = DefaultCollectors()


class WebmTLS(BaseModel):
    enabled: bool = Field(default=False, description="Enable mTLS")
    cafile: typing.Optional[FilePath] = Field(
        default=None, description="Path to the client CA file"
    )
    capath: typing.Optional[DirectoryPath] = Field(
        default=None, description="Path to the client CA directory"
    )


class WebTLS(BaseModel):
    cert: typing.Optional[FilePath] = Field(
        default=None, description="Path to the TLS certificate"
    )
    key: typing.Optional[FilePath] = Field(
        default=None, description="Path to the TLS key"
    )
    protocol: int = Field(
        default=ssl.PROTOCOL_TLS_SERVER,
        description="TLS protocol number, as described in the ssl python module",
    )
    mtls: WebmTLS = WebmTLS()

    @model_validator(mode="after")
    def tls_both_or_none(self):
        if (self.cert is None and self.key is None) or (
            self.cert and self.key
        ):
            return self
        raise ValueError("certfile and keyfile must be both set or both unset")


class Web(BaseModel):
    port: PositiveInt = Field(default=9123, description="Port to listen on")
    addr: IPv4Address = Field(
        default="0.0.0.0", description="Address to listen on"
    )
    tls: WebTLS = WebTLS()


class Config(BaseSettings):
    jsonschema: SkipJsonSchema[CliSubCommand[JSONSchema]]
    log: Log = Log()
    web: Web = Web()
    collector: Collectors = Collectors()

    model_config = SettingsConfigDict(
        case_sensitive=False,
        cli_avoid_json=True,
        cli_enforce_required=False,
        cli_hide_none_type=True,
        cli_implicit_flags=True,
        cli_parse_args=True,
        cli_prog_name="py-exporter",
        cli_ignore_unknown_args=False,
        cli_exit_on_error=True,
        cli_use_class_docs_for_groups=True,
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        env_prefix="py_exporter_",
        nested_model_default_partial_update=True,
        yaml_file=["config.yml", "config.yaml"],
    )

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: typing.Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> typing.Tuple[PydanticBaseSettingsSource, ...]:
        return (
            init_settings,
            env_settings,
            dotenv_settings,
            file_secret_settings,
            YamlConfigSettingsSource(settings_cls),
        )
