Title: Opening Unity Script Files in Emacs
Date: 2018-01-24 14:32
Slug: opening-unity-script-files-in-emacs
Tags: emacs unity
Category: emacs

![01](https://i.imgur.com/9XWvvi0.png)

I've recently embarked on a mission to fully integrate [Emacs](https://www.gnu.org/software/emacs/) with my Unity game development environment. One feature that I wanted to have is the ability to open Unity scripts and text-based files in Emacs instead of MonoDevelop. This is an easy task for supported external editors but for those who aren't (Like Emacs), doing something like this is a bit tricky.

Setting [emacsclient](https://www.gnu.org/software/emacs/manual/html_node/emacs/Invoking-emacsclient.html) as the external editor works in opening the files but the line number is not passed at all (Or is not received by emacs. [Seems to be a bug](https://forum.unity.com/threads/external-editor-arguments-issue.350473/)). This means that opening files in the Project Window works but you would not be able to to jump to lines that have errors from the Console. This, of course, is unacceptable.

![02](https://i.imgur.com/8gcVuom.png)

I've tried a number of different solutions. A lot of them are hacky but clever. There was this one option of setting a [Sublime Text proxy](https://github.com/bbbscarter/EmacsProxy) as a external editor and then having that application call Emacs with the correct line number. I was not able to make it work but the idea fascinated me. There was also one that involved using Mac OS X's Automator where you [wrap a shell script as an automator app](https://stackoverflow.com/a/1857220) and you set that as the external editor. Didn't work either but it did teach me about Automator and it's future possible uses for my environment.

Thankfully, there was one solution that worked and it involved creating a .cs file and setting up a function with OnOpenAssetAttribute callback attribute. This function is called when Unity receives a command to open an asset. From here we start a process that invokes emacsclient with the correct file and line numbers. 

Here is a short example:

	:::c#
	[OnOpenAssetAttribute()]
	public static bool OnOpenedAsset(int instanceID, int line)
	{
		UnityEngine.Object selected = EditorUtility.InstanceIDToObject(instanceID);
		string ProjectPath = System.IO.Path.GetDirectoryName(UnityEngine.Application.dataPath);
		string completeFilepath = ProjectPath + Path.DirectorySeparatorChar + AssetDatabase.GetAssetPath(selected);

		// We check if this is the type of file we can open
		if (selected.GetType().ToString() == "UnityEditor.MonoScript" ||
			selected.GetType().ToString() == "UnityEngine.Shader" ) {

			string args = "-n +" + line.ToString() + " " + completeFilepath;

			// We start a process by passing the command "emacsclient -n +linenumber filePath"
			System.Diagnostics.Process proc = new System.Diagnostics.Process();
			proc.StartInfo.FileName = "/Applications/Emacs.app/Contents/MacOS/bin/emacsclient";
			proc.StartInfo.Arguments = args;
			proc.StartInfo.UseShellExecute = false;
			proc.StartInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
			proc.StartInfo.CreateNoWindow = true;
			proc.StartInfo.RedirectStandardOutput = true;
			proc.Start();

bo			// Tell unity we have handled the opening of the file.
			return true;
		}

		// We were not able to open the file. Let unity handle the opening.
		return false;
	}

**Note:** This file needs to be placed inside an "Editor" folder within Unity in order for it to work.

[Go here](https://gist.github.com/accidentalrebel/69ac38f729e72c170a8d091b4daaec52) if you want to see a more complete and fully featured implementaition of the code above. Also, a hat tip to [this repository](https://github.com/tbriley/Atom) for the solution which was largely inspired by the [VSCode project](https://github.com/dotBunny/VSCode).

