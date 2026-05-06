--[[
 SPDX-License-Identifier: GPL-2.0
 SPDX-FileCopyrightText: 2024 Björn Bidar
 partly based of functions.lua from python-rpm-macros
--]]

--[[
   Main Package should look like this:
   %%treesitter_grammars foo bar

   Or when runtime grammar names differ from source directories:
   %%treesitter_grammars markdown=tree-sitter-markdown markdown-inline=tree-sitter-markdown-inline

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

	local treesitter_grammar_names = {}
	local treesitter_grammar_sources = {}
	local treesitter_grammar_libnames = {}
	local arg = arg_compat(arg)
	local names, sources = parse_grammar_specs(arg)

	for i, name in ipairs(names) do
		table.insert(treesitter_grammar_names, name)
		table.insert(treesitter_grammar_sources, sources[i])
		table.insert(treesitter_grammar_libnames, base_libname .. "-" .. name .. ".so")
		print("Provides: treesitter_grammar(" .. base_name .. "-" .. name .. ")\n")
	end

	rpm.define("treesitter_grammar_names " .. table.concat(treesitter_grammar_names, " "))
	rpm.define("treesitter_grammar_sources " .. table.concat(treesitter_grammar_sources, " "))
	rpm.define("treesitter_grammar_libnames " .. table.concat(treesitter_grammar_libnames, " "))
end

function treesitter_configure()
	--[[
      Generate grammar sources for all the grammars provided earlier akin
      to %configure.
   --]]
	rpm.expand("%_treesitter_macro_init")
	local grammar_sources = rpm.expand("%{treesitter_grammar_sources}"):split()

	print(rpm.expand("%treesitter_set_flags"))
	print("\n")

	if #grammar_sources > 1 then
		for _, grammar_source in ipairs(grammar_sources) do
			print("(cd " .. grammar_source .. ";tree-sitter generate)")
			print("\n")
		end
	else
		local grammar_source = grammar_sources[1] or "src"
		if grammar_source == "src" then
			print("tree-sitter generate")
		else
			print("(cd " .. grammar_source .. ";tree-sitter generate)")
		end
	end
end

function treesitter_build()
	--[[
      Similar to %make_build build all grammars if possible read from
      an alternative file instead of binding.gyp
   --]]
	rpm.expand("%_treesitter_macro_init")
	local basename = rpm.expand("%{_treesitter_grammar_base_libname}")
	local grammar_names = rpm.expand("%{treesitter_grammar_names}"):split()
	local grammar_sources = rpm.expand("%{treesitter_grammar_sources}"):split()
	local arg = arg_compat(arg)
	local left_over_args = arg[1]
	local grammar_arg_binding = ""

	if left_over_args then
		grammar_arg_binding = " -b " .. arg[1]
	end

	local treesitter_target = rpm.expand("%{treesitter_target}")

	if #grammar_names > 1 then
		for i, target in ipairs(grammar_names) do
			local source = grammar_sources[i] or target
			print(
				"eval $("
					.. treesitter_target
					.. grammar_arg_binding
					.. " -g "
					.. source
					.. ") "
					.. " -o "
					.. basename
					.. "-"
					.. target
					.. ".so ${RPM_OPT_FLAGS}"
			)
			print("\n")
		end
	else
		local target = grammar_names[1]
		local source = grammar_sources[1] or "src"
		if source == "src" then
			print(
				"eval $("
					.. treesitter_target
					.. grammar_arg_binding
					.. ") "
					.. " -o "
					.. basename
					.. "-"
					.. target
					.. ".so ${RPM_OPT_FLAGS}"
			)
		else
			print(
				"eval $("
					.. treesitter_target
					.. grammar_arg_binding
					.. " -g "
					.. source
					.. ") "
					.. " -o "
					.. basename
					.. "-"
					.. target
					.. ".so ${RPM_OPT_FLAGS}"
			)
		end
	end
end

function treesitter_install()
	--[[
      Install all previously build grammars
   --]]
	rpm.expand("%_treesitter_macro_init")
	local grammars = rpm.expand("%{treesitter_grammar_libnames}"):split()
	local install_path = rpm.expand("%{buildroot}%{_treesitter_grammardir}")
	for k, grammar in pairs(grammars) do
		print("install -Dm755 " .. grammar .. " " .. install_path .. "/" .. grammar)
		print("\n")
	end
end

function treesitter_files()
	rpm.expand("%_treesitter_macro_init")
	local grammars = rpm.expand("%{treesitter_grammar_libnames}"):split()
	local grammardir = rpm.expand("%{_treesitter_grammardir}")
	local _libdir = rpm.expand("%{_libdir}")

	if grammardir ~= _libdir then
		print(rpm.expand("%dir " .. grammardir .. "\n"))
	end

	for k, grammar in pairs(grammars) do
		print(rpm.expand(grammardir .. "/" .. grammar .. "\n"))
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
	local grammars = rpm.expand("%{treesitter_grammar_names}"):split()
	local grammar_sources = rpm.expand("%{treesitter_grammar_sources}"):split()
	local treesitter = rpm.expand("%_treesitter_base_name")

	local install_cmd_base = "install -Dm644 "
	local install_path = rpm.expand("%{buildroot}%{_treesitter_grammar_develdir}/")

	local rpm_provides_macro = ""
	--print(grammar_names)
	for k, grammar in pairs(grammars) do
		if grammar then
			rpm_provides_macro = rpm_provides_macro
				.. "Provides: treesitter_grammar_src("
				.. treesitter
				.. "-"
				.. grammar
				.. ")\n"
		end
	end
	rpm.define("_treesitter_devel_provides " .. rpm_provides_macro)

	if #grammars == 1 then
		local grammar_source = grammar_sources[1] or "src"
		local module_name = treesitter .. "-" .. grammars[1]
		local grammar_install_path = install_path .. module_name
		if grammar_source == "src" then
			print(install_cmd_base .. "grammar.js " .. grammar_install_path .. "/grammar.js")
		else
			print(install_cmd_base .. grammar_source .. "/grammar.js " .. grammar_install_path .. "/grammar.js")
		end
		print("\n")
		treesitter_devel_package_json(module_name, grammar_install_path, "./grammar.js")
		return
	end

	local arg = arg_compat(arg)

	if #arg > 0 then
		--[[ FIXME: This maybe not be the best solution if packages can have a single grammar
         but also addon files
      ]]
		--
		for arg_num = 1, #arg do
			print(
				rpm.expand(
					install_cmd_base .. arg[arg_num] .. " " .. install_path .. "%{name}/" .. arg[arg_num] .. "\n"
				)
			)
			print("\n")
		end
	end

	for i, grammar in ipairs(grammars) do
		if grammar then
			local grammar_source = grammar_sources[i] or grammar
			local grammar_js = grammar_source == "src" and "grammar.js" or (grammar_source .. "/grammar.js")
			print(
				rpm.expand(
					install_cmd_base .. grammar_js .. " " .. install_path .. "%{name}/" .. grammar .. "/grammar.js\n"
				)
			)
			print("\n")
		end
	end

	treesitter_devel_package_json(rpm.expand("%{name}"), install_path .. rpm.expand("%{name}"), nil)
end

function treesitter_devel_files()
	--[[
      Install -devel files to %%{_treesitter_grammar_develdir}
   --]]
	rpm.expand("%_treesitter_macro_init")
	local grammars = rpm.expand("%{treesitter_grammar_names}"):split()
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

	if #grammars == 1 then
		print(rpm.expand("%{_treesitter_grammar_develdir}/tree-sitter-" .. grammars[1] .. "\n"))
	else
		print(rpm.expand("%{_treesitter_grammar_develdir}/%{name}\n"))
	end
end
