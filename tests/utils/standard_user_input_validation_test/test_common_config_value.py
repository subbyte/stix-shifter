
import json
from logging import Logger
import os

class Test_Config_Confirmation():
    
    def test_config_host(self):
        host_exclusion_file_list = ["datadog","reversinglabs"]
        list_of_config_files = self._get_list_of_files("config.json", host_exclusion_file_list)
        for file in list_of_config_files:
            self._confirm_standard_host_status(json.loads(file))
    
    def _confirm_standard_host_status(self, lang_en_json):
        standard_type = "text"
        standard_regex = "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9_:/\\-]*[a-zA-Z0-9])\\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9_:/\\-]*[A-Za-z0-9])$"
        if("connection" in lang_en_json and "host" in lang_en_json["connection"]):
            assert lang_en_json["connection"]["host"]["type"] == standard_type
            assert lang_en_json["connection"]["host"]["regex"] == standard_regex
                
    def test_config_port(self):
        port_exclusion_file_list = []
        list_of_config_files = self._get_list_of_files("config.json", port_exclusion_file_list)
        for file in list_of_config_files:
            self._confirm_standard_port_status(json.loads(file))

    def _confirm_standard_port_status(self, lang_en_json):
        standard_type = "number"
        standard_min = 1
        standard_max = 65535
        if("connection" in lang_en_json and "port" in lang_en_json["connection"]):
            assert lang_en_json["connection"]["port"]["type"] == standard_type
            assert lang_en_json["connection"]["port"]["min"] == standard_min
            assert lang_en_json["connection"]["port"]["max"] == standard_max
            assert "placeholder" not in lang_en_json["connection"]["host"]
            
    def test_config_self_signed(self):
        port_exclusion_file_list = []
        list_of_config_files = self._get_list_of_files("config.json", port_exclusion_file_list)
        for file in list_of_config_files:
            self._confirm_standard_self_signed_status(json.loads(file))

    def _confirm_standard_self_signed_status(self, lang_en_json):
        standard_type = "password"
        standard_optional = True
       
        if("connection" in lang_en_json and "selfSignedCert" in lang_en_json["connection"]):
            assert lang_en_json["connection"]["selfSignedCert"]["type"] == standard_type
            assert lang_en_json["connection"]["selfSignedCert"]["optional"] == standard_optional
                
    def _get_list_of_files(self, file_name, exclusion_list):
        #Generated by WCA for GP
        #Here's an example of how you can do this in Python using the os module:

        # Define the directory path
        directory_path = os.getcwd() + "/stix_shifter_modules"
        lang_en_file_list = list()
        
        # Iterate through all the child directories
        for dir_name, subdir_list, file_list in os.walk(directory_path):
            # Check if the file exists in the current directory
            if file_name in file_list:
                # Open the file and read its contents
                with open(os.path.join(dir_name, file_name), 'r') as file:
                    excluded = False
                    for excluded_file in exclusion_list:
                        if(excluded_file in file.name):
                            excluded = True
                            break
                    if(not excluded):
                        lang_en_file_list.append(file.read())                      
        return lang_en_file_list