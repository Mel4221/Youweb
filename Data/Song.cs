using QuickTools.QCore;
using System;
using System.Net;
using System.Text.RegularExpressions;
namespace Youweb.Data
{

        public class Song 
        {
                public override string ToString()
                {
                        return  $"Title: {this.Title}\n"+
                                $"RName: {this.RName}\n"+
                                $"Duration: {this.Duration}\n"+
                                $"YTLink: {this.YTLink}\n"+
                                $"IconLink: {this.IconLink}"+
                                $"IconLinkTemp: {this.IconLinkTemp}";
                }
                public string Title{get;set;} = string.Empty;
                public string RName {get;set;} = string.Empty; 

                public string YTLink{get;set;} = string.Empty;
                public string IconLink{get;set;} = string.Empty;
                public string IconLinkTemp{get;set;} = string.Empty; 
                public string Duration{get;set;} = string.Empty;
                
                public static string SubRoot()
                {
                    string root, slashes;
                    slashes = "";
                    root = System.IO.Path.Combine(System.IO.Directory.GetCurrentDirectory(), "wwwroot")+Get.Slash();
                    foreach(char ch in root)
                    {
                        if(ch == Get.Slash()[0])
                        {
                            slashes += $"..{Get.Slash()}";
                        }
                    }

                    return slashes;
                }
                public static string CleanName(string path)
                {
                        string valid_file_name, 
                        no_more_than_2_spaces,
                        no_underscore_at_the_end,
                        too_many_underscore,
                        no_spaces_at_the_end,
                        final;

                        valid_file_name = Regex.Replace(path, @"[\x00-\x1F\x7F-\x9F\[\]\(\)\x80-\xFF]", " ");

                        no_more_than_2_spaces = Regex.Replace(valid_file_name, @"\s{2,}", " ");
                                        
                        too_many_underscore = Regex.Replace(no_more_than_2_spaces, @"_{2,}", "_");

                        no_spaces_at_the_end = Regex.Replace(too_many_underscore, @"\s+(?=\.[^.]*$)", "");

                        no_underscore_at_the_end = Regex.Replace(no_spaces_at_the_end, @"_(?=\.[^.]*$)", "");

                        final = no_underscore_at_the_end;

                        return final;
                }
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