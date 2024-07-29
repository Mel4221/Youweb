using QuickTools.QCore;
using System;
using System.Net;
namespace Youweb.Data
{

        public class Song 
        {
                public string YTLink{get;set;} = string.Empty;
                public string IconLink{get;set;} = string.Empty;
                public string Duration{get;set;} = string.Empty;
                public string Title{get;set;} = string.Empty;
                public static bool IsValidLink(string link)
                {
                        Uri uriResult;
                        bool result = Uri.TryCreate(link, UriKind.Absolute, out uriResult) 
    && (uriResult.Scheme == Uri.UriSchemeHttp || uriResult.Scheme == Uri.UriSchemeHttps);
                        return result;
                }
                public static string ParseTime(string duration)
                {
                        if(Get.IsNumber(duration))
                        {
                            double number =  Math.Round((double.Parse(duration) / 60),2);
                            
                            return number.ToString().Replace(".",":");
                        }else
                        {
                                return duration;
                        }
                }
                public static bool IsAudio(string fileName)
                {
                        if (Get.FileExention("opus") == "opus" || 
                                Get.FileExention("aiff") == "aiff" || 
                                Get.FileExention("m4a") == "m4a" || 
                                Get.FileExention("alac") == "alac" || 
                                Get.FileExention("wma") == "wma" || 
                                Get.FileExention("ogg") == "ogg" || 
                                Get.FileExention("flac") == "flac" || 
                                Get.FileExention("aac") == "aac" || 
                                Get.FileExention("wav") == "wav" || 
                                Get.FileExention("mp3") == "mp3"
                        )
                        {
                                return true;
                        }else{
                                return false; 
                        }
 

                }
        }
}