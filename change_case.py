import sublime
import sublime_plugin
import re

SETTINGS = ["title_case_ignore"]
MERGE_KEYS = []


class ChangeCaseTitleCaseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        settings = get_settings(view, "ChangeCase")
        self.ignore_list = settings.get("title_case_ignore")

        regions = view.sel()
        for region in regions:
            region = view.word(region)
            replace_string = ""
            substr = view.substr(region)
            newline_split = re.split("\n", substr)
            for line in newline_split:
                space_split_words = re.split(' ', line)

                out = [self.proper_case_word(space_split_words[0], True)]

                for word in space_split_words[1:]:
                    out.append(self.proper_case_word(word))
                if replace_string != "":
                    replace_string += "\n"
                replace_string += " ".join(out)
            view.replace(edit, region, replace_string)

    def proper_case_word(self, string, beginning=False):
        ret = ""
        if beginning:
            string = string.capitalize()
        if "-" in string:
            sub_words = re.split("-", string)
            word_list = [sub_words[0].capitalize()]
            for temp in sub_words[1:]:
                word_list.append(self.word_conversion(temp))
            ret = "-".join(word_list)
        else:
            ret = self.word_conversion(string)
        return ret

    def word_conversion(self, word):
        if word in self.ignore_list:
            return word
        else:
            return word.capitalize()


def get_settings(view, plugin_name):
    settings = sublime.load_settings("%s.sublime-settings" % plugin_name)
    project_settings = {}
    local_settings = {}
    if view != None:
        project_settings = view.settings().get(plugin_name, {})

    for setting in SETTINGS:
        local_settings[setting] = settings.get(setting)

    for key in project_settings:
        if key in SETTINGS:
            if key in MERGE_KEYS:
                local_settings[key] = dict(local_settings[key].items() + project_settings.get(key).items())
            else:
                local_settings[key] = project_settings[key]
        else:
            print "%s[Warning]: Invalid key '" + key + "' in project settings." % plugin_name

    return local_settings
