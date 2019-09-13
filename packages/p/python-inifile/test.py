from inifile import IniFile

i = IniFile('hello.ini')
i['foo.bar'] = 'testing more stuff'
i['foo.mup'] = 'aha!'
print i.get_updated_lines()
i.save()
