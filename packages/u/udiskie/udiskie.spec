#
# spec file for package udiskie
#
# Copyright (c) 2024 SUSE LLC
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


Name:           udiskie
Version:        2.5.3
Release:        0
Summary:        Removable disk automounter for udisks
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/coldfix/udiskie
Source:         https://files.pythonhosted.org/packages/source/u/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  fdupes
# Needed for typelib() - Requires.
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxslt-tools
BuildRequires:  python-rpm-macros
# Runtime dependencies:
BuildRequires:  python3-gobject
BuildRequires:  python3-setuptools
BuildRequires:  typelib(Gtk) = 3.0
BuildRequires:  typelib(Notify)
Requires:       gdk-pixbuf-loader-rsvg
Requires:       python3-PyYAML
Requires:       python3-docopt
Requires:       python3-gobject
Requires:       python3-setuptools
Requires:       python3-xml
Requires:       udisks2
Requires:       typelib(Gtk) = 3.0
Recommends:     %{name}-lang
# this package does not exist on Tumbleweed and conflicts with python311-keyring-keyutils whose module is also named 'keyutils'
Recommends:     python3-keyutils
BuildArch:      noarch

%description
udiskie is a UDisks front-end that allows to manage removeable media such as CDs
or flash drives from userspace. Its features include:

- automount removable media when inserted
- notifications (on insertion, mount, unmount, …)
- GTK tray icon to manage all available devices
- command line tools for manual un-/mounting
- support for LUKS encrypted devices
- password caching
- works with either udisks1 or udisks2
- an extensible code base (python)
- a maintainer who is open for suggestions;)

%lang_package

%prep
%autosetup
# work-around Python error in easy_install.py (setuptools)
sed -e '/ScriptWriter.template/s/^/#/g' -i setup.py

%build
%python3_build

%install
%python3_install

make %{?_smp_mflags} -C doc
install -Dm 0644 doc/%{name}.8 %{buildroot}%{_mandir}/man8/%{name}.8
# Create man pages for other binaries
for other in %{name}-mount %{name}-umount %{name}-info; do
  echo ".so man8/%{name}.8" > %{buildroot}%{_mandir}/man8/"${other}.8"
done

%fdupes %{buildroot}%{python3_sitelib}/%{name}/
%fdupes %{buildroot}%{_mandir}/man8/

%find_lang %{name}

%files
%doc CHANGES.rst README.rst
%license COPYING
%{_bindir}/%{name}*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-*-py%{py3_ver}.egg-info
%{_mandir}/man?/%{name}*.?%{ext_man}
%{_datadir}/zsh/site-functions/_udiskie*
%{_datadir}/bash-completion/completions/*

%files lang -f %{name}.lang

%changelog
