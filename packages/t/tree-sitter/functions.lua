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
