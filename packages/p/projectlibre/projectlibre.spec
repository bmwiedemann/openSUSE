#
# spec file for package projectlibre
#
# Copyright (c) 2021 SUSE LLC
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


Name:           projectlibre
Version:        1.9.3
Release:        0
Summary:        Project Management Tool
License:        CPAL-1.0
Group:          Productivity/Office/Management
URL:            https://www.projectlibre.org
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Source2:        %{name}.png
Source3:        x-%{name}.desktop
BuildRequires:  ant
BuildRequires:  update-desktop-files
Requires:       java >= 1.6.0
BuildArch:      noarch

%description
ProjectLibre is a project manager which is compatible with Microsoft
Project 2003, 2007 and 2010 files. It has Gantt charts, PERT charts,
network diagrams and Earned Value Costing.

%prep
%setup -q

%build
#Set the file encoding for source files
export JAVA_TOOL_OPTIONS=-Dfile.encoding=cp1252
cd projectlibre_build/
ant clean
ant

%install
export NO_BRP_CHECK_BYTECODE_VERSION=true
mkdir -p %{buildroot}%{_datadir}/%{name}/lib
install -Dm0755 projectlibre_contrib/*.jar %{buildroot}%{_datadir}/%{name}/lib/
install -Dm0755 projectlibre_build/dist/%{name}.jar %{buildroot}%{_datadir}/%{name}/

# startscript
cat > %{name} << EOF
#!/bin/sh
#
echo Starting %{name} version %{version} ...
echo with options : \${@}

java -jar %{_datadir}/%{name}/%{name}.jar \${@}

EOF

# Install startscript
install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}

# Install desktop file and icon with -i switch ;)
%suse_update_desktop_file -i %{name}

%files
%license projectlibre_build/license/*
%doc projectlibre_build/doc/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

%changelog
