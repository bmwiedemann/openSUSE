#
# spec file for package lua-lmod
#
# Copyright (c) 2025 SUSE LLC
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
%define _buildshell /bin/bash

%if "%flavor" == ""
%endif

%if "%flavor" == "doc-pdf"
%define build_pdf 1
%endif

ExcludeArch:    i586 %arm s390

%define lmod_min_lua_version 5.1
%define version_name_suffix() %{lua: x=string.gsub(rpm.expand("%*"),"([0-9]+)%.([0-9]+).*","%1%2"); print(x)}
%{!?lua_pref:%define lua_pref lua}

%define lua_lmod_modulesdir %{_datarootdir}/lmod/modulefiles
%define lua_lmod_admin_modulesdir %{_datarootdir}/lmod/admin/modulefiles
%define lua_lmod_moduledeps %{_datarootdir}/lmod/moduledeps
%define lua_path ?.lua;?/?.lua;%{lua_noarchdir}/?.lua;%{lua_noarchdir}/?/init.lua
%define lua_cpath ?.so;?/?.so;%{lua_archdir}/?.so
%{!?_rpmmacrodir:%define _rpmmacrodir %_rpmconfigdir/macros.d}

Name:           lua-lmod
Summary:        Lua-based Environment Modules used in HPC
License:        MIT
Group:          Development/Libraries/Other
Version:        8.7.55
Release:        0
URL:            https://github.com/TACC/Lmod
Source0:        https://github.com/TACC/Lmod/archive/%{version}.tar.gz#$/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
#Patch1:         Messages-Remove-message-about-creating-a-consulting-ticket.patch
#Patch2:         Doc-Ugly-workaround-for-bug-in-Sphinx.patch

BuildRequires:  %{lua_pref} >= %{lmod_min_lua_version}
BuildRequires:  %{lua_pref}-devel >= %{lmod_min_lua_version}
BuildRequires:  %{lua_pref}-luafilesystem
BuildRequires:  %{lua_pref}-luaposix
BuildRequires:  %{lua_pref}-luaterm
BuildRequires:  bc
BuildRequires:  procps
BuildRequires:  tcl
# Do not require a lua interpreter directly, this will be handled implicitly
Requires:       lua%{version_name_suffix %lua_version}-luafilesystem
Requires:       lua%{version_name_suffix %lua_version}-luaposix
Requires:       lua%{version_name_suffix %lua_version}-luaterm
Requires:       tcl
Requires:       (lua-lmod-apparmor-abstractions if apparmor-abstractions)
Conflicts:      Modules
BuildRequires:  python3-Sphinx
Provides:       environment-modules
Provides:       lua-lmod-man = %{version}-%{release}
Provides:       ml = %{version}
Conflicts:      environment-modules
%if 0%{?build_pdf:1}

BuildRequires:  python3-Sphinx-latex
BuildRequires:  texlive
BuildRequires:  texlive-babel
BuildRequires:  texlive-babel-english
BuildRequires:  texlive-capt-of
BuildRequires:  texlive-caption
BuildRequires:  texlive-cmap
BuildRequires:  texlive-courier
BuildRequires:  texlive-dvips
BuildRequires:  texlive-eqparbox
BuildRequires:  texlive-fancybox
BuildRequires:  texlive-fancyhdr
BuildRequires:  texlive-fancyvrb
BuildRequires:  texlive-framed
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-latexmk
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-mdwtools
BuildRequires:  texlive-multirow
BuildRequires:  texlive-needspace
BuildRequires:  texlive-parskip
BuildRequires:  texlive-psnfss
BuildRequires:  texlive-tex-gyre
BuildRequires:  texlive-threeparttable
BuildRequires:  texlive-times
BuildRequires:  texlive-titlesec
BuildRequires:  texlive-upquote
BuildRequires:  texlive-varwidth
BuildRequires:  texlive-wrapfig
%endif # %%build_pdf

%description
Lmod is an Environment Module System as used in High Performance Computing
(HPC) based on Lua, Reads TCL Modules, Supports a Software Hierarchy.
Environment Modules are to select the individual versions of HPC libraries
and tools from a set of installed ones.
It requires these libraries and tools to be available in separate independent
directory structures. On SUSE systems default location for these structures
is under /usr/lib/hpc.

It is not recommended to install this tool on systems which do not belong
to an HPC deployment which uses the module system.

%package doc
Summary:        Documentation for Lmod
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Documentation (pdf) for the Lmod Environment Modules System.

%package apparmor-abstractions
Summary:        Apparmor bash Abstraction for Lmod
BuildRequires:  apparmor-abstractions
BuildRequires:  apparmor-rpm-macros
Requires:       apparmor-abstractions
BuildArch:      noarch

%description apparmor-abstractions
Profile for shell source scripts for lua-lmod

%prep
%setup -q -n Lmod-%{version}
%autopatch -p1
# Remove message about creating a consulting ticket
sed -i -e '/[T,t]icket/d' messageDir/*.lua

%build
%if 0%{!?build_pdf:1}
export LUA_CPATH="%{lua_cpath}"
export LUA_PATH="%{lua_path}"
%configure --prefix=%{_datadir} \
    --with-module-root-path=%{lua_lmod_modulesdir} \
    --libdir=%{lua_archdir} \
    --datadir=%{lua_noarchdir} \
    --with-redirect=yes \
    --with-autoSwap=no \
    --with-fastTCLInterp=no
make
find my_docs/ -name .gitignore -delete
%endif
cd docs; make %{?build_pdf:latexpdf} %{!?build_pdf:man}; cd ..

%install
%if 0%{!?build_pdf:1}
export LUA_CPATH="%{lua_cpath}"
export LUA_PATH="%{lua_path}"
%make_install

mkdir -p %{buildroot}%{_rpmmacrodir}/rpm
cat <<EOF > %{buildroot}%{_rpmmacrodir}/macros.lmod
%%lua_lmod_modulesdir %{lua_lmod_modulesdir}
%%lua_lmod_admin_modulesdir %{lua_lmod_admin_modulesdir}
%%lua_lmod_moduledeps %{lua_lmod_moduledeps}
EOF
mkdir -p %{buildroot}%{lua_lmod_modulesdir}
mkdir -p %{buildroot}%{lua_lmod_admin_modulesdir}
mkdir -p %{buildroot}%{lua_lmod_moduledeps}
mkdir -p %{buildroot}/%{_mandir}/man1

# Fix file duplicates
rm -f %{buildroot}/%{_datadir}/lmod/%{version}/init/ksh
ln -s %{_datadir}/lmod/%{version}/init/sh  %{buildroot}/%{_datadir}/lmod/%{version}/init/ksh
rm -f %{buildroot}/%{_datadir}/lmod/%{version}/init/zsh
ln -s %{_datadir}/lmod/%{version}/init/bash  %{buildroot}/%{_datadir}/lmod/%{version}/init/zsh
rm -f %{buildroot}/%{_datadir}/lmod/%{version}/init/tcsh
ln -s %{_datadir}/lmod/%{version}/init/csh %{buildroot}/%{_datadir}/lmod/%{version}/init/tcsh
rm -f %{buildroot}/%{_datadir}/lmod/%{version}/settarg/Version.lua
ln -s %{_datadir}/lmod/%{version}/libexec/Version.lua %{buildroot}/%{_datadir}/lmod/%{version}/settarg/Version.lua

for file in $(find %{buildroot}%{_datadir}/lmod/%{version}/init -type f); do
    sed -i -e "/#!.*/d" $file
    chmod a-x $file
done
for file in $(find %{buildroot}%{_datadir}/lmod); do
    [ -f "$file" ] || continue
    line=$(head -1 $file)
    if [[ $line =~ \#\!.*bin/env ]]; then
	case $line in
	    *bash) newline="#! /bin/bash" ;;
	    *) newline="#! /usr/bin/${line##*/env* }" ;;
	esac
	sed -i "1s,^.*,${newline}\n," $file
    fi
done
mkdir -p %{buildroot}/%{_sysconfdir}/profile.d
cat <<EOF >%{buildroot}/%{_sysconfdir}/profile.d/lmod.sh
# -*- shell-script -*-
########################################################################
#  This is the system wide source file for setting up
#  modules:
#
########################################################################

# NOOP if running under known resource manager
if [ ! -z "\$SLURM_NODELIST" ];then
     return
fi

export LMOD_SETTARG_CMD=":"
export LMOD_FULL_SETTARG_SUPPORT=no
export LMOD_COLORIZE=no
export LMOD_PREPEND_BLOCK=normal

if [ \$EUID -eq 0 ]; then
    export MODULEPATH=\${MODULEPATH:+\${MODULEPATH}:}%{?OHPC_MODULES:%{OHPC_ADMIN}/modulefiles:%{OHPC_MODULES}:}%{lua_lmod_admin_modulesdir}:%{lua_lmod_modulesdir}
else
    export MODULEPATH=\${MODULEPATH:+\${MODULEPATH}:}%{?OHPC_MODULES:%{OHPC_MODULES}:}%{lua_lmod_modulesdir}
fi

export BASH_ENV=%{_datadir}/lmod/%{version}/init/bash

# Initialize modules system
. \${BASH_ENV} >/dev/null

# Load baseline SUSE HPC environment
module try-add suse-hpc

EOF

cat <<EOF >%{buildroot}/%{_sysconfdir}/profile.d/lmod.csh
# -*- shell-script -*-
########################################################################
#  This is the system wide source file for setting up
#  modules:
#
########################################################################

if ( \$?SLURM_NODELIST ) then
    exit 0
endif

setenv LMOD_SETTARG_CMD ":"
setenv LMOD_FULL_SETTARG_SUPPORT "no"
setenv LMOD_COLORIZE "no"
setenv LMOD_PREPEND_BLOCK "normal"

if ( \${?MODULEPATH} ) then
   setenv MODULEPATH "\${MODULEPATH}:"
else
   setenv MODULEPATH ""
endif

if ( \`id -u\` == "0" ) then
   setenv MODULEPATH "\${MODULEPATH}%{?OHPC_MODULES:%{OHPC_ADMIN}/modulefiles:%{OHPC_MODULES}:}%{lua_lmod_admin_modulesdir}:%{lua_lmod_modulesdir}"
else
   setenv MODULEPATH "\${MODULEPATH}%{?OHPC_MODULES:%{OHPC_MODULES}:}%{lua_lmod_modulesdir}"
endif

# Initialize modules system
source %{_datadir}/lmod/%{version}/init/csh >/dev/null

# Load baseline SUSE HPC environment
module try-add suse-hpc

EOF
install -d -m755 %{buildroot}%{_sysconfdir}/apparmor.d/abstractions/bash.d
cat <<EOF > %{buildroot}%{_sysconfdir}/apparmor.d/abstractions/bash.d/lmod
   abi <abi/3.0>,

   %_datadir/lmod/%{version}/init/*    r,
   %_datadir/lmod/%{version}/libexec/addto ix,
EOF

mkdir -p %{buildroot}/%{_mandir}/man1
install -p -m644 docs/build/man/lmod.1 %{buildroot}/%{_mandir}/man1/
%endif

%posttrans apparmor-abstractions
rm -rf /var/cache/apparmor/* 2>/dev/null
systemctl is-active -q apparmor && systemctl reload apparmor ||:

%if 0%{!?build_pdf:1}
%files
%license License
%doc README.*
%config %{_sysconfdir}/profile.d/lmod.sh
%config %{_sysconfdir}/profile.d/lmod.csh
%dir %{_datadir}/lmod
%dir %{lua_lmod_modulesdir}
%dir %{lua_lmod_admin_modulesdir}
%dir %{lua_lmod_moduledeps}
%{_rpmmacrodir}/macros.lmod
%{_datadir}/lmod/*
%{_mandir}/man1/lmod.1.*

%files apparmor-abstractions
%dir %{_sysconfdir}/apparmor.d/abstractions/bash.d
%{_sysconfdir}/apparmor.d/abstractions/bash.d/lmod
%endif

%if 0%{?build_pdf}
%files doc
%doc my_docs/*.txt my_docs/*.pdf my_docs/*.md
%doc docs/build/latex/Lmod.pdf
%endif

%changelog
