--[[
 SPDX-License-Identifier: GPL-2.0
 SPDX-FileCopyrightText: 2024 Björn Bidar
 partly based of functions.lua from python-rpm-macros
--]]


--[[
   Main Package should look like this:
   %%treesitter_grammars foo bar

   %%build
   %%treesitter_configure
   %%treesitter_build

   %%install
   %%treesitter_install

   %%files
   %%treesitter_files
--]]


function treesitter_grammars()
   --[[
      Define any grammars to be included inside the package
   --]]
   rpm.expand("%_treesitter_macro_init")
   local base_name = rpm.expand("%_treesitter_base_name")
   local base_libname = rpm.expand("%_treesitter_grammar_base_libname")

   local treesitter_grammar_names = ""
   local treesitter_grammar_libnames = ""

   local arg = arg
   local suse_version = tonumber(rpm.expand("%suse_version"))
   if suse_version < 1600 then
      arg = arg_compat()
   end

   for arg_num = 1,#arg do
      treesitter_grammar_libnames=treesitter_grammar_libnames .. base_libname .. "-" .. arg[arg_num] .. ".so "
   end
   rpm.define("treesitter_grammar_libnames " .. treesitter_grammar_libnames)

   for arg_num = 1,#arg do
      treesitter_grammar_names=treesitter_grammar_names .. " " .. arg[arg_num]
      print("Provides: treesitter_grammar(" .. base_name .. "-" .. arg[arg_num] .. ")\n")
   end
   rpm.define("treesitter_grammar_names " .. treesitter_grammar_names)
end


function treesitter_configure()
   --[[
      Generate grammar sources for all the grammars provided earlier akin
      to %configure.
   --]]
   rpm.expand("%_treesitter_macro_init")
   local grammars = string.split(rpm.expand("%{treesitter_grammar_names}"))

   print(rpm.expand("%treesitter_set_flags"))
   print("\n")

   if #grammars > 1 then
      for k,grammar in pairs(grammars) do
         print("(cd " .. grammar .. ";tree-sitter generate)")
         print("\n")
      end
   else
      print("tree-sitter generate")
   end

end

function treesitter_build()
   --[[
      Similar to %make_build build all grammars if possible read from
      an alternative file instead of binding.gyp
   --]]
   rpm.expand("%_treesitter_macro_init")
   local basename = rpm.expand("%{_treesitter_grammar_base_libname}")
   local grammar_names = rpm.expand("%treesitter_grammar_names")
   local arg = arg
   local suse_version = tonumber(rpm.expand("%suse_version"))
   if suse_version < 1600 then
      arg = arg_compat()
   end
   local left_over_args = arg[1]
   local grammar_arg_binding = ""


   if left_over_args then
      grammar_arg_binding=" -b "..arg[1]
   end

   local treesitter_target = rpm.expand("%{treesitter_target}")
   local grammar_names_tbl = string.split(grammar_names, " ")

   if #grammar_names_tbl > 1 then
      for k,target in pairs(grammar_names_tbl) do
         print("eval $(" .. treesitter_target .. grammar_arg_binding .. " -g " .. target ..") " .. " -o " .. basename .. "-" .. target .. ".so ${RPM_OPT_FLAGS}")
         print("\n")
      end
   else
      print("eval $(" .. treesitter_target .. grammar_arg_binding .. ") " .. " -o " .. basename.. "-" .. grammar_names .. ".so ${RPM_OPT_FLAGS}")
   end
end



function treesitter_install()
   --[[
      Install all previously build grammars
   --]]
   rpm.expand("%_treesitter_macro_init")
   local grammars = string.split(rpm.expand("%{treesitter_grammar_libnames}"))
   local install_path = rpm.expand("%{buildroot}%{_treesitter_grammardir}")
   for k,grammar in pairs(grammars) do
      print("install -Dm755 " .. grammar .. " " .. install_path .. "/" .. grammar)
      print("\n")
   end
end

function treesitter_files()
   rpm.expand("%_treesitter_macro_init")
   local grammars = string.split(rpm.expand("%{treesitter_grammar_libnames}"))
   local grammardir = rpm.expand("%{_treesitter_grammardir}")
   local _libdir = rpm.expand("%{_libdir}")

   if not grammardir == libdir then
      print(rpm.expand("%dir " .. grammardir.."\n"))
   end

   for k,grammar in pairs(grammars) do
      print(rpm.expand(grammardir .. "/"..grammar.."\n"))
   end
end

--[[
   Optional -devel package for grammars that are needed for other grammars to be built.

   If the -devel package is needed it should look like this:
   %%install
   [...] # Main page here

   %%treesitter_devel_install

   # Or if the package has shared files between grammars:
   %%treesitter_devel_install foobar.js

   %%treesitter_devel_package
--]]

function treesitter_devel_install()
   --[[
      Install all grammars sources defined earlier.
      If passed these can also include additional files such as shared fragments
      that are used between multiple grammars in the same package.
   --]]
   rpm.expand("%_treesitter_macro_init")
   --local grammar_names = rpm.expand("%{treesitter_grammar_names}")
   local grammars = string.split(rpm.expand("%{treesitter_grammar_names}"))
   local treesitter = rpm.expand("%_treesitter_base_name")

   local install_cmd_base = "install -Dm644 "
   local install_path = rpm.expand("%{buildroot}%{_treesitter_grammar_develdir}/")

   local rpm_provides_macro = ""
   --print(grammar_names)
   for k,grammar in pairs(grammars) do
      if grammar then
         rpm_provides_macro=rpm_provides_macro.. "Provides: treesitter_grammar_src(" ..treesitter .. "-" .. grammar ..")\n"
      end
   end
   rpm.define("_treesitter_devel_provides "..rpm_provides_macro)

   if #grammars == 1 then
      print(install_cmd_base .. "grammar.js " .. install_path .. treesitter .. "-" .. grammars[1].. "/grammar.js")
      return
   end

   local arg = arg
   local suse_version = tonumber(rpm.expand("%suse_version"))
   if suse_version < 1600 then
      arg = arg_compat()
   end

   if #arg > 0 then
      --[[ FIXME: This maybe not be the best solution if packages can have a single grammar
         but also addon files
      ]]--
      for arg_num = 1,#arg do
         print(rpm.expand(install_cmd_base  .. arg[arg_num] .. " " .. install_path .. "%{name}/" .. arg[arg_num] .. "\n"))
         print("\n")
      end
   end

   for k,grammar in pairs(grammars) do
      if grammar then
         print(rpm.expand(install_cmd_base .. grammar .. "/grammar.js " .. install_path .. "%{name}/" .. grammar .. "/grammar.js\n"))
         print("\n")
      end
   end
end


function treesitter_devel_files()
   --[[
      Install -devel files to %%{_treesitter_grammar_develdir}
   --]]
   rpm.expand("%_treesitter_macro_init")
   local grammars = string.split(rpm.expand("%{treesitter_grammar_names}"))
   local grammar_develdir = rpm.expand("%{_treesitter_grammar_develdir}")
   local fpp

   print(rpm.expand("%dir %{_treesitter_grammar_develdir} \n"))
   --[[
      Own all directories leading up to %%_includedir which we include in
      %%_treesitter_grammar_develdir
   --]]
   while not (grammar_develdir == rpm.expand("%_includedir")) do
      print(rpm.expand("%dir " .. grammar_develdir .. "\n"))
      grammar_develdir = grammar_develdir:dirname()
   end
   print(rpm.expand("%{_treesitter_grammar_develdir}/%{name}\n"))
end
