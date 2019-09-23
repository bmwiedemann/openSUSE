# encoding: utf-8

require "json"

module Yast
  class GetcountrydataClient < Client
    def main
      Yast.import "Language"
      Yast.import "Keyboard"
      Yast.import "Console"
      Yast.import "OSRelease"

      langs = Language.GetLanguagesMap(true)
      
      consolefonts = nil
      datafilepath = Directory.find_data_file("consolefonts.json")

      if datafilepath.nil?
        consolefonts = SCR.Read(path(".target.yast2"), "consolefonts_#{OSRelease.id}.ycp")
        consolefonts ||= SCR.Read(path(".target.yast2"), "consolefonts.ycp")
      else
        consolefonts = JSON.load(File.read(datafilepath))
      end

      timezonemap = Language.GetLang2TimezoneMap(true)

      dir = ENV["OUTPUTDIR"]
      raise "OUTPUTDIR is not set" unless dir

      Builtins.foreach(langs) do |lang, ll|
        suffix = ll[2] || ""
        fqlanguage = lang + suffix
        kbd = Keyboard.GetKeyboardForLanguage(lang, "us")
        # does not really set keyboard, only fills some data
        Keyboard.SetKeyboard(kbd)
        consolefont = consolefonts[fqlanguage] || consolefonts[lang]
        if consolefont.nil? && lang.size > 2
          consolefont = consolefonts[lang[0,2]]
        end
        consolefont ||= []
        if consolefont.is_a?(Hash)
            font = consolefont["font"] || ""
            unicodeMap = consolefont["unicodeMap"] || ""
            screenMap = consolefont["screenMap"] || ""
            magic = consolefont["magic"] || ""
        else
            font = consolefont[0] || ""
            unicodeMap = consolefont[1] || ""
            screenMap = consolefont[2] || ""
            magic = consolefont[3] || ""
        end
        timezone = timezonemap[lang] || ""
        contents =
          "RC_LANG='#{fqlanguage}'\n" +
          "CONSOLE_FONT='#{font}'\n" +
          "CONSOLE_SCREENMAP='#{screenMap}'\n" +
          "CONSOLE_UNICODEMAP='#{unicodeMap}'\n" +
          "CONSOLE_MAGIC='#{magic}'\n" +
          "KEYTABLE='#{Keyboard.keymap}'\n" +
          "TIMEZONE='#{timezone}'\n"

        contents << "RC_LC_MESSAGES='zh_TW.UTF-8'\n" if lang == "zh_HK"
        SCR.Write(path(".target.string"), dir + "/" + fqlanguage, contents)
      end
    end
  end
end

Yast::GetcountrydataClient.new.main
