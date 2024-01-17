#
# spec file for package godot-rpm-macros
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           godot-rpm-macros
Version:        1
Release:        0
Summary:        RPM macros for Godot
License:        MIT
Group:          Development/Tools/Building
URL:            https://godotengine.org/
Source0:        macros.godot
Source1:        rpmlintrc
Requires:       coreutils
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Provides RPM macros that will allow for easier packaging of games made with 
the Godot engine.

%prep

%build

%install
install -D -p -m 644 %{S:0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.godot

%files
%defattr(-,root,root)
%dir %{_rpmconfigdir}/macros.d/
%{_rpmconfigdir}/macros.d/macros.godot

%changelog
