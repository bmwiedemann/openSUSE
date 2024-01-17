#!/usr/bin/lua
-- Usage: $0 sitelib filebasename

-- From https://stackoverflow.com/a/60172017/164233
-- Split a string into a table using a delimiter and a limit
string.split = function(str, pat, limit)
  local t = {}
  local fpat = "(.-)" .. pat
  local last_end = 1
  local s, e, cap = str:find(fpat, 1)
  while s do
    if s ~= 1 or cap ~= "" then
      table.insert(t, cap)
    end

    last_end = e+1
    s, e, cap = str:find(fpat, last_end)

    if limit ~= nil and limit <= #t then
      break
    end
  end

  if last_end <= #str then
    cap = str:sub(last_end)
    table.insert(t, cap)
  end

  return t
end


local buildroot=os.getenv('RPM_BUILD_ROOT')
local subroot=buildroot:len() + 1
local fnamebase = arg[1]

local pkg_file = ''

-- Create a line of .lang file for each .mo file
for line in io.stdin:lines() do
    pkg_file = line:sub(subroot)
    if pkg_file:find(fnamebase .. "$") then
        print("%lang(" .. pkg_file:split('/')[8] .. ") " .. pkg_file)
    else
        print(pkg_file)
    end
end
