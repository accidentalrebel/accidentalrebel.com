Title: Making Unity beep after scripts finish reloading
Date: 2020-05-01 17:07
Slug: making-unity-beep-after-scripts-finish-reloading
Tags: dev, unity, 
Category: dev

Our latest game, HistoHunters, has grown into a really big project that compilation now takes a really long time. Longer than no sane programmer wants it to be. It has gotten so bad that changing a single file would take about a minute for recompilation! 

Thankfully, I have managed to shorten this wait time through the use of [assembly definitions](https://docs.unity3d.com/Manual/ScriptCompilationAssemblyDefinitionFiles.html). If you have a big Unity project and compile times are slow, this is the solution to that. Just for kicks I also [purchased an SSD](http://karlo.licudine.me/computery-has-evolved-.html) and that also helped reduce compile times (Not much as the assembly definitions though).

However, in spite of these changes compiling still takes a few seconds to reload scripts. This seems to be the lowest it could go. While this is definitely better, I can't help but feel that the seconds spent waiting is wasted.

I recently got the idea of having Unity inform me when a script has finished reloading. Instead of informing me visually, I decided that it would be betetr for it to play a beep sound. With this, I could use the time to rest my eyes and relax. Once it beeps then I'm back to working again. It's such a simple thing but my eyes welcome every little bit of rest.

Here's the code that I use if you are interested. Note that this is an editor script so it should be placed inside any "Editor" folder for it to run.

	:::c#
	using System.Collections;
	using System.Collections.Generic;
	using UnityEngine;
	using UnityEditor;
	using System.Diagnostics;

	public class BuildManager : MonoBehaviour
	{
		[UnityEditor.Callbacks.DidReloadScripts]
		private static void OnScriptsReloaded() 
		{
			EditorApplication.Beep();
		}
	}
	
Since I'm using Linux the above line does not work for me. Here's a different version that spawns a OS process and runs the `play` command. Be sure to have [sox](http://sox.sourceforge.net/) installed on your Linux machine.

	:::c#
	ProcessStartInfo proc = new ProcessStartInfo();
	proc.FileName = "play";
	proc.Arguments = "-q -n synth 0.1 sin 880 vol 0.2";
	proc.WindowStyle = ProcessWindowStyle.Minimized;
	proc.CreateNoWindow = true;
	Process.Start(proc);

Of course, this is definitely not a solution to the problem. I'd still have to wait. But what I like about this is that it has turned a negative into a positive. And that is always great.
