import os
import re
import sys
import json


# $PR_NUMBER "$PR_AUTHOR" "$GITHUB_TOKEN"

class Process_pr():
    def __init__(self, pr_number, pr_author):
        self.__pr_number = pr_number
        self.__pr_author = pr_author

    def author(self):
        return self.__pr_author

    def number(self):
        return self.__pr_number

    def command(self, cmd, save_output=True):
        try:
            if save_output:
                return json.loads(os.popen(cmd).read())
            else:
                os.system(cmd)
        except json.decoder.JSONDecodeError:
            print('PR doesn\'t exist. Exiting process!')
            exit()

    def assign_intern(self, ivy_intern):
        self.command(f"gh pr edit {self.__pr_number} --add-assignee {ivy_intern}", save_output=False)

    def assign_random_intern(self, intern_list):
        random_intern = rn.choice(intern_list)
        self.command(f"gh pr edit {self.__pr_number} --add-assignee {random_intern}", save_output=False)
        print(f'[+] {random_intern} was assigned to PR {self.__pr_number}')
