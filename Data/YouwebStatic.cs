using QuickTools.QCore;
namespace Youweb.Data
{
        public static class YouwebStatic
        {
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