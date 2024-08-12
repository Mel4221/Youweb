using QuickTools.QCore;
using System.Diagnostics;
using System.IO; 
namespace Youweb.Data
{
        public static class YouwebStatic
        {
                public static bool ActionCompleted { get; set; } = false;
                
                public static string GetRoot(string path)
                {
                    string dir = Path.Combine(GetRoot(), path)+Get.Slash(); 
                    if (!Directory.Exists(dir)){
                        Directory.CreateDirectory(dir);
                        return dir; 
                    }else{
                        return dir; 
                    }
                }
                public static string GetRoot()
                {
                    string path = Path.Combine(Directory.GetCurrentDirectory(), "wwwroot")+Get.Slash(); 
                    if(path == Get.Slash())
                    {
                        path = "wwwroot";
                        return path;
                    }else
                    {
                        return path;
                    }
                }
        private static string PythonFileName()
                {
                    string python, file;
         
                        file = Path.Combine(GetRoot("python"), "python.config");


                        if(File.Exists(file))
                        {
                            python = File.ReadAllText(file);
                            if(!string.IsNullOrEmpty(python))
                            {
                                return python;
                            }
                        }if(Get.IsWindow()){
                                python = "python";
                                return python;
                        }else{
                                python = "python3";
                                return python;
                        }

                   
                }
                public static ProcessStartInfo StartInfo(string arguments)
                {
                        return new ProcessStartInfo()
                        {
                                FileName=PythonFileName(),
                                Arguments=$"{System.IO.Path.Combine(System.IO.Directory.GetCurrentDirectory(), "wwwroot")}{Get.Slash()}you{Get.Slash()}main.py {arguments}",
                                RedirectStandardOutput = true,
                                UseShellExecute = false, // Required for redirection
                                CreateNoWindow = true // Optional: do not create a window
                        };
                }

                public static bool HasDownloadInProgress {get;set;} = false; 
                public static string CurrentAction{get;set;} = string.Empty; 
                public static Check Check {get;set;}
                //private static Thread NotificationThread;

                public static bool HasActions()
                {
                        //Get.Yellow($"Has Actions: {YouwebStatic.HasDownloadInProgress}");
                        return YouwebStatic.HasDownloadInProgress;
                }
                /*
                public static void Notify()
                {
                        while(HasDownloadInProgress)
                        {
                                Get.Pink($"Running an Action: [{CurrentAction}]");
                                Get.WaitTime(500);
                        }
                }
                */
                public static void Start(string action)
                {
                        Check = new Check();
                        //NotificationThread = new Thread(Notify);

                        Check.Start(); 

                        YouwebStatic.CurrentAction = action; 
                        YouwebStatic.HasDownloadInProgress = true; 
                        //Get.Yellow($"Action Started: {YouwebStatic.CurrentAction} Status: {YouwebStatic.HasDownloadInProgress}");
                        //NotificationThread.Start();

                }
                public static void Stop()
                {
                        if(YouwebStatic.HasActions())
                        {
                                Get.Yellow($"Time Elapsed: {Check.Stop()}");
                                YouwebStatic.CurrentAction = string.Empty; 
                                YouwebStatic.HasDownloadInProgress = false;
                                Get.Red($"Action Stoped: {YouwebStatic.CurrentAction} Action in Progress: {YouwebStatic.HasDownloadInProgress}"); 
                                return;
                        }else{
                                Get.Yellow("No Action in progress...");
                        }
                }
        }
}