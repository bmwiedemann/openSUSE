--[[
   SPDX-License-Identifier: GPL-2.0
   SPDX-FileCopyrightText: 2024 Björn Bidar

   partly based of functions.lua from python-rpm-macros
--]]

-- declare common functions
function string.startswith(str, prefix)
   return str:sub(1, prefix:len()) == prefix
end

function string.endswith(str, suffix)
   return str:sub(-suffix:len()) == suffix
end

function string.dirname(str)
   if str:match("(.*)/") == "" then
      return nil
   else
      return str:match("(.*)/")
   end
end

function string.basename(str)
   while true do
      local idx = str:find("/")
      if not idx then return str end
      str = str:sub(idx + 1)
   end
end

function string.split(str, sep)
   if sep == nil then
      sep = '%s'
   end

   local res = {}
   local func = function(w)
      table.insert(res, w)
   end

   string.gsub(str, '[^'..sep..']+', func)
   return res
end

function arg_compat(arg)
   --[[
      Compat macro as workaround for older rpm not having function
      arguments available as table arg(uments)

      If that's not required just return arg
   --]]

   local suse_version = tonumber(rpm.expand("%suse_version"))
   if suse_version > 1600 then
      return arg
   end

   local arg_count = rpm.expand("%#")
   local arg = {}

   for arg_num = 1,arg_count do
      arg[arg_num] = rpm.expand(("%" .. arg_num))
   end

   return arg
end

function parse_grammar_specs(specs)
   local names = {}
   local sources = {}
   local multi_grammar = #specs > 1

   for _, spec in ipairs(specs) do
      local name, source = spec:match("^([^=]+)=(.+)$")
      if not name then
         name = spec
         if multi_grammar then
            source = name
         else
            source = "src"
         end
      end

      table.insert(names, name)
      table.insert(sources, source)
   end

   return names, sources
end
