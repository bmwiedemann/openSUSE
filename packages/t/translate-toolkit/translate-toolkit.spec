#
# spec file for package translate-toolkit
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define modname translate-toolkit
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define binaries pocompile build_firefox.sh build_tmdb buildxpi.py csv2po csv2tbx flatxml2po get_moz_enUS.py html2po ical2po idml2po ini2po json2po junitmsgfmt moz2po mozlang2po odf2xliff oo2po oo2xliff php2po phppo2pypo po2csv po2flatxml po2html po2ical po2idml po2ini po2json po2moz po2mozlang po2oo po2php po2prop po2rc po2resx po2sub po2symb po2tiki po2tmx po2ts po2txt po2web2py po2wordfast po2xliff po2yaml poclean pocommentclean pocompendium poconflicts pocount podebug pofilter pogrep pomerge pomigrate2 popuretext poreencode porestructure posegment posplit poswap pot2po poterminology pretranslate prop2po pydiff pypo2phppo rc2po resx2po sub2po symb2po tbx2po tiki2po tmserver ts2po txt2po web2py2po xliff2odf xliff2oo xliff2po yaml2po
%define manpages pocompile build_firefox.sh csv2po csv2tbx flatxml2po html2po idml2po ini2po json2po junitmsgfmt moz2po mozlang2po odf2xliff oo2po oo2xliff phppo2pypo po2csv po2flatxml po2html po2idml po2ini po2json po2moz po2mozlang po2oo po2prop po2rc po2resx po2sub po2symb po2tiki po2tmx po2ts po2txt po2web2py po2wordfast po2xliff poclean poconflicts podebug pofilter pogrep pomerge porestructure posegment poswap pot2po poterminology pretranslate prop2po pypo2phppo rc2po resx2po sub2po symb2po tbx2po tiki2po translatetoolkit ts2po txt2po web2py2po xliff2odf xliff2oo xliff2po
Name:           translate-toolkit%{psuffix}
Version:        3.1.1
Release:        0
Summary:        Tools and API to assist with translation and software localization
License:        GPL-2.0-or-later
URL:            https://toolkit.translatehouse.org/
Source:         https://github.com/translate/translate/releases/download/%{version}/%{modname}-%{version}.tar.gz
Patch0:         xliff-xsd-no-network.patch
# PATCH-FIX-UPSTREAM versioned_executables.patch mcepl@suse.com
# Use versioned partially installed executables
Patch1:         versioned_executables.patch
Patch2:         sphinx-intersphinx.patch
BuildRequires:  %{python_module Levenshtein >= 0.12}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module beautifulsoup4 >= 4.3}
# extra modules here are needed for manpages
BuildRequires:  %{python_module cheroot >= 8.3.0}
BuildRequires:  %{python_module iniparse >= 0.5}
BuildRequires:  %{python_module lxml >= 4.0}
BuildRequires:  %{python_module phply >= 1.2.5}
BuildRequires:  %{python_module ruamel.yaml >= 0.16.12}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vobject >= 0.9.6.1}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gettext-runtime
BuildRequires:  git-core
BuildRequires:  iso-codes
BuildRequires:  python-rpm-macros
Requires:       gettext-runtime
Requires:       python
Requires:       python-lxml >= 4.0
Requires:       python-pycountry >= 19.8.18
Requires:       python-pyenchant >= 3.1.1
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
# The following are for the full experience of translate-toolkit
Recommends:     gaupol
Recommends:     iso-codes
Recommends:     python-Levenshtein >= 0.12
Recommends:     python-aeidon >= 1.7.0
Recommends:     python-beautifulsoup4 >= 4.3
Recommends:     python-chardet >= 3.0.4
Recommends:     python-cheroot >= 8.3.0
Recommends:     python-iniparse >= 0.5
Recommends:     python-phply >= 1.2.5
Recommends:     python-pyparsing >= 2.4.7
Recommends:     python-ruamel.yaml >= 0.16.10
Recommends:     python-vobject >= 0.9.6.1
Provides:       translate-toolkit = %{version}-%{release}
Obsoletes:      translate-toolkit < %{version}-%{release}
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module aeidon >= 1.7.0}
BuildRequires:  %{python_module chardet >= 3.0.4}
BuildRequires:  %{python_module pycountry >= 19.8.18}
BuildRequires:  %{python_module pyenchant >= 3.1.1}
BuildRequires:  %{python_module pyparsing >= 2.4.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module translate-toolkit >= %{version}}
BuildRequires:  %{python_module xml}
BuildRequires:  subversion
%endif
%python_subpackages

%description
The Translate Toolkit is a set of software and documentation designed to help
make the lives of localizers both more productive and less frustrating.

The software includes programs to convert localization formats to the common
PO, and emerging XLIFF format.  There are also programs to check and manage PO
and XLIFF files.  Online documentation includes guides on using the tools,
running a localization project and how to localize various projects from
OpenOffice.org to Mozilla.

At its core the software contains a set of classes for handling various
localization storage formats: DTD, properties, OpenOffice.org GSI/SDF,
CSV, MO, Qt .ts, TMX, TBX, WordFast txt, Gettext .mo, Windows RC, and
of course PO and XLIFF.  It also provides scripts to convert between
these formats.

Also part of the Toolkit are Python programs to create word counts, merge
translations and perform various checks on translation files.

%package devel-doc
Summary:        Tools and API to assist with translation and software localization
Requires:       %{name} = %{version}
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}
BuildArch:      noarch

%description devel-doc
The %{name}-devel-doc package contains Translate Toolkit API documentation for developers wishing to build new tools for the
toolkit or to use the libraries in other localization tools.

%prep
%setup -q -n %{modname}-%{version}
%autopatch -p1

sed -i 296"s|'share'|'translate/share'|" setup.py

#Fix for shebang errors:
for lib in translate/{*.py,*/*.py,*/*/*.py}; do
 sed -i '\|%{_bindir}/env |d' $lib
done

find . -name jquery.js -exec dos2unix '{}' \;

%build
%if !%{with test}
%python_build

pushd docs
# Can't use parallel build here!
%make_build -j1 html man
#no hidden files
find _build -name '.?*' -delete
popd
%endif

%install
%if !%{with test}
%python_install

# create manpages
mkdir -p %{buildroot}%{_mandir}/man1
for program in %{buildroot}%{_bindir}/*; do
    case $(basename $program) in
      pocompendium|poen|pomigrate2|popuretext|poreencode|posplit|pocount|poglossary|lookupclient.py|tmserver|build_tmdb)
        ;;
      *)
        MPAGE="%{buildroot}%{_mandir}/man1/$(basename $program).1"
        LC_ALL=C PYTHONPATH=. $program --manpage > "$MPAGE" || rm -f "$MPAGE"
        ;;
    esac
done
install -m 644 docs/_build/man/* %{buildroot}%{_mandir}/man1/

# move documentation files to datadir
%{python_expand install -d -m 755 %{buildroot}%{_defaultdocdir}/%{modname}
mv %{buildroot}%{$python_sitelib}/translate/docs/_build/html %{buildroot}%{_defaultdocdir}/%{modname}
rm -rf %{buildroot}%{$python_sitelib}/translate/docs
rm -rf %{buildroot}home/abuild/.local/lib/python%{$python_version}/site-packages/
}

# create symlinks for man pages
%fdupes -s %{buildroot}%{_mandir}
# create hardlinks for the rest
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Prepare alternatives
for mpage in %{manpages} ; do
%python_clone -a %{buildroot}%{_mandir}/man1/$mpage.1
done
for binary in %{binaries} ; do
%python_clone -a %{buildroot}%{_bindir}/$binary
done
%endif

%check
%if %{with test}
export PYTHONDONTWRITEBYTECODE=1
%pytest
%endif

%post

%define my_install_alternatives() %{lua:\
    function file_exists(path) \
    	local f = io.open(path) \
    	if f == nil then return false \
    	else f:close() return true  \
    	end \
    end \
    local t={} \
    local manpath = "" \
    for str in string.gmatch(rpm.expand("%**"), "([^%s]+)") do \
            table.insert(t, str) \
    end \
    local bindir = rpm.expand("%{_bindir}") \
    local mandir = rpm.expand("%{_mandir}") .. "/man1" \
    local ver_ext = "-" .. t[1] \
    local man_ext = ".1" .. rpm.expand("%{?ext_man}") \
    local man_ext_ver = ver_ext .. man_ext \
    \
    local ua_cmd = "update-alternatives --install " .. mandir .. "/translatetoolkit" .. man_ext .. " translatetoolkit.1 " .. \
        mandir .. "/translatetoolkit" .. man_ext_ver .. " 20 \\\\\\n" \
    local elems = table.pack(table.unpack(t, 2)) \
    for arg, name in ipairs(elems) do \
        ua_cmd = ua_cmd .. " --slave " .. bindir .. "/" .. name .. " " .. name .. " " .. bindir .. "/" .. name .. ver_ext .. " \\\\\\n" \
        manpath = mandir .. "/" .. name .. man_ext_ver \
        if file_exists(manpath) then \
            ua_cmd = ua_cmd .. " --slave " .. mandir .. "/" .. name .. man_ext .. " " .. name .. ".1 " .. manpath .. " \\\\\\n" \
        end \
    end\
    -- we need to remove the last backslash and EOL \
    print(ua_cmd:sub(1, -3)) \
}
%my_install_alternatives %{_rec_macro_helper}%{lua:expand_macro("version")} %{binaries}

%postun
if [ ! -f %{_mandir}/man1/translatetoolkit-%{_rec_macro_helper}%{lua:expand_macro("version")}.1%{?ext_man} ] ; then
   update-alternatives --remove translatetoolkit %{_mandir}/man1/translatetoolkit-%{_rec_macro_helper}%{lua:expand_macro("version")}.1%{?ext_man}
fi

%if !%{with test}
%files %{python_files}
%dir %{_defaultdocdir}/%{modname}
%{_defaultdocdir}/%{modname}/html/
%exclude %{_defaultdocdir}/%{modname}/html/api
%exclude %{_defaultdocdir}/%{modname}/html/_sources
%license COPYING
%doc README.rst
%ghost %{_sysconfdir}/alternatives/*
%{_bindir}/*
%{_mandir}/man1/*
%{python_sitelib}/translate
%{python_sitelib}/translate_toolkit-%{version}-*.egg-info

%files devel-doc
%doc %{_defaultdocdir}/%{modname}/html/api
%doc %{_defaultdocdir}/%{modname}/html/_sources
%endif

%changelog
