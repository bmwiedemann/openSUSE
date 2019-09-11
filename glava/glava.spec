#
# spec file for package glava
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           glava
Version:        1.6.3
Release:        0
Summary:        OpenGL audio spectrum visualizer
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Visualization
URL:            https://github.com/wacossusca34/glava
Source:         https://github.com/wacossusca34/glava/archive/v%{version}.tar.gz
BuildRequires:  gcc
#BuildRequires:  libglfw-devel >= 3.1
BuildRequires:  libXcomposite-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libpulse-devel
#See: https://github.com/wacossusca34/glava/issues/100
Requires:       libglvnd-devel

%description
OpenGL audio spectrum visualizer. Its primary use case is for desktop windows or backgrounds.

%prep
%setup -q

%build
#ENABLE_GLFW=1 make %{?_smp_mflags}
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_sysconfdir}/xdg/glava/
%{_bindir}/glava

%changelog
