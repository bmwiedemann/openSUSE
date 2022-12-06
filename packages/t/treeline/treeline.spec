#
# spec file for package treeline
#
# Copyright (c) 2022 SUSE LLC
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


Name:           treeline
Version:        3.1.5
Release:        0
Summary:        Versatile Tree-Style Outliner for Defining Custom Data Schemas
License:        GPL-2.0-or-later
Group:          Productivity/Office/Other
URL:            https://treeline.bellz.org
Source0:        https://github.com/doug-101/TreeLine/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        x-%{name}.desktop
Source2:        x-%{name}-gz.desktop
Source3:        x-treepad.desktop
Source99:       treeline-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  perl
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
Requires:       python3-qt5
BuildArch:      noarch

%description
TreeLine is a versatile tool for working with all kinds of information
that fit into a tree-like structure.

It can be used to edit bookmark files, create mini-databases (for
example, for addresses, tasks, records, or CDs), outline documents, or
just collect ideas. It can also be used as a generic editor for XML
files.

The data schemas for any node in the data tree can be customized and
new types of nodes can be defined. The way data is presented on the
screen, exported to HTML, or printed can be defined with HTML-like
templates. Plug-ins can be written to load and save data from and to
custom file formats or external data sources and extend the
functionality of TreeLine.

TreeLine is written in Python and uses the PyQt bindings to the Qt
toolkit, which makes it very portable.

%prep
%setup -q -n TreeLine
for i in source/*.py; do
  sed -i "s|#!%{_bindir}/env python|#!%{_bindir}/python|g" "$i"
done

find source/ -type f -name '*.py' | while read f; do
    case $f in
    */treeline.py) continue;;
    esac
    perl -i -n -e 'print unless m,^#!, and 1..1' "$f"
done

%build

%install
python3 install.py -x \
   -p "%{_prefix}" \
   -i "%{_datadir}/%{name}/icons" \
   -d "%{_docdir}/%{name}" \
   -b %{buildroot}

python3 -c "import compileall; compileall.compile_dir('%{buildroot}%{_libexecdir}/treeline',2,ddir='%{_libexecdir}/treeline')"

install -d "%{buildroot}%{_datadir}/mimelnk/application"
install -m0644 \
    "%{SOURCE1}" \
    "%{SOURCE2}" \
    "%{SOURCE3}" \
    "%{buildroot}%{_datadir}/mimelnk/application/"

%suse_update_desktop_file -i treeline Office ProjectManagement

%fdupes -s "%{buildroot}%{_datadir}"

rm -f %{buildroot}%{_docdir}/%{name}/{INSTALL,LICENSE}

%files
%license doc/LICENSE
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%dir %{_datadir}/mimelnk
%dir %{_datadir}/mimelnk/application
%doc %{_docdir}/%{name}
%{_bindir}/treeline
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/treeline-icon.png
%{_datadir}/icons/hicolor/scalable/apps/treeline-icon.svg
%{_datadir}/mimelnk/application/x-treeline-gz.desktop
%{_datadir}/mimelnk/application/x-treeline.desktop
%{_datadir}/mimelnk/application/x-treepad.desktop
%{_datadir}/treeline/

%changelog
