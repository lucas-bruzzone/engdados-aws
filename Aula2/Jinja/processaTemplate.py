import jinja2
import yaml
import os

'ENVIRONMENT' in os.environ

def renderiza_template():
    with open('Aula2/Jinja/redshift.yml.j2', 'r') as f:
        redshift_yaml = f.read()

    with open('Aula2/Jinja/config.yml', 'r') as f:
        config = yaml.safe_load(f)


    redshift_template = jinja2.Template(redshift_yaml)
    redshift_rendered = redshift_template.render({**config, **os.environ})

    with open('Aula2/Jinja/redshift.yml', 'w') as f:
        f.write(redshift_rendered)

renderiza_template()