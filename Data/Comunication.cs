using System.Text.Json;
using Newtonsoft.Json.Linq;
using Newtonsoft.Json;
using System;
using System.IO;
using System.Diagnostics;
namespace Youweb.Data
{

        public class UMessage
        {
                public string RName {get;set;}
                public string Action{get;set;}
                public string Type{get;set;} 
                public string Arguments{get;set;}
                public override string ToString()
                {
                        return $"RName: {this.RName}\nAction: {this.Action}\nType: {this.Type}\nArguments: {this.Arguments}\n";
                }
        }
        public partial class UShare
        {
                public string Target{get;set;}
                public UShare(string target){this.Target = target;}
                public UMessage Message{get;set;} 
                public async Task Send(UMessage message)
                {
                        this.Message = message; 
                        await this.Send(); 
                }

                public async Task<Song> Check(string target)
                {
                        this.Target = target;    
                        return await Check(); 
                }
                public async Task<Song> Check()
                {
                        return await Task<Song>.Run(async ()=>{

                                return new Song();
                        }); 
                }
                public async Task Send()
                {
                        
                        JMetadata meta = new JMetadata(this.Target);
                        meta.SetValue("rname",this.Message.RName);
                        meta.SetValue("action",this.Message.Action);
                        meta.SetValue("type",this.Message.Type);
                        meta.SetValue("arguments",this.Message.Arguments);


                        return;
                        Process process = Process.Start(YouwebStatic.StartInfo(this.Target));
                        //wait that the whole process is completed
                        string output = process.StandardOutput.ReadToEnd();

                        string logs = Path.Combine(YouwebStatic.GetRoot("out"), $"{this.Message.RName}.out");

                        process.WaitForExit();
                        //if (!File.Exists(logs)) File.Create(logs);
                        output += $"\nExit Code: {process.ExitCode}\n";
                        output += $"\nLog Time: {DateTime.Now.ToString("MM/dd/yyyy hh:mm:ss")}\n";

                        File.AppendAllText(logs, output);

                  
                }

        }
}