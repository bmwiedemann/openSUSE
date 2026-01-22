#
# spec file for package virtui-manager
#
# Copyright (c) 2026 SUSE LLC
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

Name:           virtui-manager
Version:        0.9.9
Release:        1
Summary:        Terminal-based interface to manage virtual machines using libvirt
License:        GPL-3.0-or-later
URL:            https://aginies.github.io/virtui-manager/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-base
BuildRequires:  python3-setuptools
# Runtime dependencies
Requires:       python3-libvirt-python
Requires:       python3-textual >= 0.40.0
Requires:       python3-PyYAML
Requires:       python3-markdown-it-py
BuildArch:      noarch

%description
Virtui-manager is a terminal-based interface to manage virtual machines using libvirt.
It allows you to view VM status, start/stop/pause VMs, and access consoles.

%package doc
Summary:        Documentation for virtui-manager
Group:          Documentation/HTML

%description doc
This package contains the HTML documentation for virtui-manager.

%package -n virtui-remote-viewer
Summary:        Simple remote viewer for virtui-manager
Requires:       %{name} = %{version}
Requires:       python3-gobject
Requires:       python3-libvirt-python
Requires:       gtk3
#Requires:       libgtk-vnc-2_0-0
#Requires:       libvirt-glib-1_0-0
# Spice support (optional but good to have)
Recommends:     typelib(SpiceClientGtk) = 3.0

%description -n virtui-remote-viewer
A simple remote viewer application bundled with virtui-manager.
It supports VNC and SPICE protocols.

%prep
%setup -q
rm -vf src/vmanager/.gitignore
rm -vf srv/vmanager/virtui-remote-viewer_gtk4.py

%build
# No build required for pure python source install strategy
# We verify the build works though
# python3 -m build --wheel --no-isolation || true

%install
# Install the application source to /usr/share/virtui-manager
mkdir -p %{buildroot}%{_datadir}/virtui-manager
cp -a src/vmanager %{buildroot}%{_datadir}/virtui-manager/

# Create binary wrappers
mkdir -p %{buildroot}%{_bindir}

# virtui-manager wrapper
cat > %{buildroot}%{_bindir}/virtui-manager <<EOF
#!/bin/sh
export PYTHONPATH=%{_datadir}/virtui-manager
cd %{_datadir}/virtui-manager/vmanager
exec python3 vmanager.py "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/virtui-manager

# virtui-manager-cmd wrapper
cat > %{buildroot}%{_bindir}/virtui-manager-cmd <<EOF
#!/bin/sh
export PYTHONPATH=%{_datadir}/virtui-manager
cd %{_datadir}/virtui-manager/vmanager
exec python3 vmanager_cmd.py "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/virtui-manager-cmd

# virtui-remote-viewer wrapper
cat > %{buildroot}%{_bindir}/virtui-remote-viewer <<EOF
#!/bin/sh
export PYTHONPATH=%{_datadir}/virtui-manager
cd %{_datadir}/virtui-manager/vmanager
exec python3 virtui-remote-viewer.py "\$@"
EOF
chmod +x %{buildroot}%{_bindir}/virtui-remote-viewer

# Install docs
mkdir -p %{buildroot}%{_docdir}/%{name}/html
if [ -d docs ]; then
    cp -r docs/* %{buildroot}%{_docdir}/%{name}/html/
fi
# Install other docs
cp README.md FEATURES.md %{buildroot}%{_docdir}/%{name}/

# Deduplicate files
%fdupes %{buildroot}%{_datadir}/virtui-manager
%fdupes %{buildroot}%{_docdir}/%{name}

%files
%license LICENSE
%doc README.md FEATURES.md
%{_bindir}/virtui-manager
%{_bindir}/virtui-manager-cmd
%dir %{_datadir}/virtui-manager
%{_datadir}/virtui-manager/vmanager

%files doc
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/html

%files -n virtui-remote-viewer
%{_bindir}/virtui-remote-viewer

%changelog
