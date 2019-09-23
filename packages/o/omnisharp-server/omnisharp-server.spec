#
# spec file for package omnisharp-server
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           omnisharp-server
Version:        0+git.1440884867.e190291
Release:        0
License:        MIT
Summary:        HTTP wrapper around NRefactory allowing C# editor plugins
Url:            https://github.com/OmniSharp/omnisharp-server
Group:          Development/Libraries
Source:         %{name}-%{version}.tar.xz
BuildRequires:  mono-devel
PreReq:         mono-core
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Otherwise Mono(Nancy) is added as PreReq
AutoReqProv:    no
BuildArch:      noarch

%description
HTTP wrapper around NRefactory allowing C# editor plugins to be written for any
editor in any language.

This is the server component for the Vim OmniSharp plugin, YouCompleteMe,
Sublime Text 2, Sublime Text 3, Emacs OmniSharp plugin and Atom plugin

%prep
%setup -q -n %{name}-%{version}

%build
if [[ -d build ]]; then
    rm -rf build
fi
mkdir build
xbuild OmniSharp.sln /p:TargetFrameworkVersion="v4.5" /p:Configuration=Release /property:OutputPath='%{_builddir}/%{buildsubdir}/build' /t:build

%install
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -vr %{_builddir}/%{buildsubdir}/build/*  %{buildroot}%{_libexecdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/OmniSharp <<EOF
#!/bin/sh
exec -a OmniSharp mono "%{_libexecdir}/%{name}/OmniSharp.exe" "\$@"
EOF

%files
%defattr(-,root,root)
%doc LICENSE.md README.md
%{_libexecdir}/%{name}
%attr(0655,root,root) %{_bindir}/OmniSharp

%changelog

