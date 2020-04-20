import os

#About is always made
os.makedirs("/Defs", exist_ok=True)
os.makedirs("/Languages", exist_ok=True)
os.makedirs("/Textures", exist_ok=True)

{% if(cookiecutter.version_control != 'n') %}
os.system("rw-release init \"{{cookiecutter.mod_name.replace(' ', '')}}\" \"{{cookiecutter.short_desc}}\"")
os.system("rw-release create {{cookiecutter.mod_ver}}")
os.system("rw-release use {{cookiecutter.mod_ver}}")
{% endif %}