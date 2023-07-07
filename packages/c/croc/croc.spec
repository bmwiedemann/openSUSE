#
# spec file for package croc
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2021 Orville Q. Song <orville@anislet.dev>
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


%global provider        github
%global provider_tld    com
%global project         schollz
%global repo            croc
%global provider_prefix %{provider}.%{provider_tld}/%{project}
%global import_path     %{provider_prefix}/%{repo}

Name:           croc
Version:        9.6.5
Release:        0
Summary:        Easily and securely send things from one computer to another
License:        MIT
Group:          Networking/File transfer
URL:            https://github.com/schollz/croc
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        %{name}.service
BuildRequires:  golang-packaging
BuildRequires:  golang(API) >= 1.20

%{go_nostrip}
%{go_provides}

%description
croc could easily and securely send things from one computer to another.

%prep
%setup -q -n %{name}-%{version}
%setup -a1 %{SOURCE1}

%build
%goprep .
mkdir -p vendor/%{provider_prefix}
ln -s . vendor/%{import_path}
%gobuild -ldflags "-s -w" .

%install
%goinstall
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-,root,root)
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_unitdir}/%{name}.service

%changelog
