#
# spec file for package gnome-games-scripts
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-games-scripts
Version:        3.8.0
Release:        0
Summary:        Build helpers for gnome game packages
License:        MIT
Group:          Amusements/Games/Other
URL:            http://www.gnome.org
Source0:        gnome-games-create-post
BuildArch:      noarch

%description
gnome-games-scripts is nothing more than a helper package producing
the post scriptlets for various gnome-games descendents.

The script does not serve much purpose out of this usecase.

%prep

%build

%install
install -m 0755 -d %{buildroot}%{_bindir}
install -m 755 %{SOURCE0} %{buildroot}%{_bindir}/

%files
%{_bindir}/gnome-games-create-post

%changelog
