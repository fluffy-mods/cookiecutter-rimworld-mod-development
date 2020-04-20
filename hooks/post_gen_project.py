import os

#About is always made
os.makedirs("/Defs", exist_ok=True)
os.makedirs("/Languages", exist_ok=True)
os.makedirs("/Textures", exist_ok=True)

{% if(cookiecutter.harmony != 'n') %}
os.system("pushd Source && dotnet restore && popd")
{% endif %}

{% if(cookiecutter.version_control != 'n') %}

# stuff specifically for my release script(s);
# create repository on fluffy-mods
os.system("rw-release init \"{{cookiecutter.mod_name.replace(' ', '')}}\" \"{{cookiecutter.short_desc}}\"")

# update/create generated files
os.system("mod update")

# create release branch for mod version
os.system("rw-release create {{cookiecutter.mod_ver}}")

# set upstream and use branch as default
os.system("rw-release use {{cookiecutter.mod_ver}}")
{% endif %}