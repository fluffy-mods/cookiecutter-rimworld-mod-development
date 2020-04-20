using System.Reflection;
using System.Linq;
using Verse;
using RimWorld;
using UnityEngine;
{%if(cookiecutter.harmony != 'n')%}using HarmonyLib;
{%endif%}
namespace {{cookiecutter.mod_name.replace(' ', '')}}
{
	public class Mod : Verse.Mod
	{
		public Mod(ModContentPack content) : base(content)
		{
{%if(cookiecutter.settings != 'n')%}			// initialize settings
			GetSettings<Settings>();

{%endif%}{%if(cookiecutter.harmony != 'n')%}
#if DEBUG
			Harmony.DEBUG = true;
#endif
			Harmony harmony = new Harmony("{{cookiecutter.author}}.{{cookiecutter.mod_name.replace(' ', '')}}");
			harmony.PatchAll();
{%endif%}		}
{%if(cookiecutter.settings != 'n')%}
		public override void DoSettingsWindowContents(Rect inRect)
		{
			base.DoSettingsWindowContents(inRect);
			GetSettings<Settings>().DoWindowContents(inRect);
		}

		public override string SettingsCategory()
		{
			return "{{cookiecutter.mod_name}}";
		}
{% endif %}	}
}