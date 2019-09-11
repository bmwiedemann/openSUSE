#
# spec file for package fly
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


Name:           fly
Version:        2.0.1
Release:        0
Summary:        A Script to Create PNGs
License:        SUSE-Permissive
Group:          Productivity/Graphics/Visualization/Other
Url:            http://martin.gleeson.com/fly/
# Mirror is used since martin gleeson (master site) rejects robot requests
Source:         http://www.w3perl.com/fly/dist/%{name}-%{version}.tar.gz
Patch1:         fly-2.0.0-gif.patch
BuildRequires:  dos2unix
BuildRequires:  gd-devel

%description
Fly allows you to create images with script statements. It uses gdlib.

%prep
%setup -q
%patch1
# Gifs are not supported
rm -fr examples/gif

# Duplicate file in source
rm -f examples/jpeg/small-end.fly

# Use unix line endings
dos2unix README examples/{jpeg,png,perl}/* examples/example.csh

%build
make %{?_smp_mflags} CFLAGS="%{optflags}" CC="gcc" LIBS="-lgd"

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 fly %{buildroot}%{_bindir}

%files
%doc README examples doc
%{_bindir}/fly

%changelog
