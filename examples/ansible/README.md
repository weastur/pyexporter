# Ansible

[**This is just an example, not a production ready solution**]

Fix hosts inventory file, then deploy

```shell
ansible-playbook -i hosts playbook.yml
```

This will install python with venv, create venv, python package, create systemd unit and enable/sytart it.

P.S. You need to have `ansible` installed on your machine.
