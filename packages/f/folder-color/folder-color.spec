#
# spec file for package folder-color
#
# Copyright (c) 2020 SUSE LLC
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


%define _name   folder_color
Name:           folder-color
Version:        0.0.88
Release:        0
Summary:        File browser extension for changing directory colors in Caja, Nautilus and Nemo
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/costales/folder-color
Source:         https://launchpad.net/~costales/+archive/ubuntu/folder-color/+files/%{name}-common_%{version}.tar.gz
Source1:        https://launchpad.net/~costales/+archive/ubuntu/folder-color/+files/%{name}_%{version}.tar.gz
Source2:        https://launchpad.net/~costales/+archive/ubuntu/folder-color/+files/%{name}-caja_%{version}.tar.gz
Source3:        https://launchpad.net/~costales/+archive/ubuntu/folder-color/+files/%{name}-nemo_%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python3
BuildRequires:  python3-distutils-extra
BuildArch:      noarch

%description
A file browser extension for choosing the color of a folder.

%package -n nautilus-extension-%{name}
Summary:        Nautilus extension for changing directory color
Group:          Productivity/File utilities
Requires:       %{name}-common = %{version}
Requires:       nautilus
Requires:       python3-nautilus
# folder-color-nautilus was last used in openSUSE Leap 42.1.
Provides:       %{name}-nautilus = %{version}
Obsoletes:      %{name}-nautilus < %{version}

%description -n nautilus-extension-%{name}
A file browser extension for choosing the color of a folder.

%package -n caja-extension-%{name}
Summary:        Caja extension for changing directory color
Group:          Productivity/File utilities
Requires:       %{name}-common = %{version}
Requires:       caja
Requires:       python-caja
# folder-color-caja was last used in openSUSE Leap 42.1.
Provides:       %{name}-caja = %{version}
Obsoletes:      %{name}-caja < %{version}

%description -n caja-extension-%{name}
A file browser extension for choosing the color of a folder.

%package -n nemo-extension-%{name}
Summary:        Nemo extension for changing directory color
Group:          Productivity/File utilities
Requires:       %{name}-common = %{version}
Requires:       nemo
Requires:       python-nemo

%description -n nemo-extension-%{name}
A file browser extension for choosing the color of a folder.

%package common
Summary:        Auxiliary files for the folder-color file browser extension
Group:          Productivity/File utilities
Requires:       gtk3-tools
Requires:       gvfs
Recommends:     %{name}-common-lang = %{version}

%description common
A file browser extension for choosing the color of a folder.

%lang_package -n %{name}-common

%prep
%setup -qn common -a1 -a2 -a3

chmod a-x COPYING.GPL3
sed -i '/name/s/%{name}/%{name}-nautilus/' nautilus/setup.py

%build
# Nothing to build.

%install
for dir in . nautilus caja nemo; do
    pushd $dir
    python3 setup.py install \
      --root=%{buildroot} --prefix=%{_prefix}
    popd
done
%fdupes %{buildroot}%{_datadir}
%find_lang %{name}-common

%files -n nautilus-extension-%{name}
%license COPYING.GPL3
%{_datadir}/nautilus-python/
%{python3_sitelib}/%{_name}_nautilus-*

%files -n caja-extension-%{name}
%license COPYING.GPL3
%{_datadir}/caja-python/
%{python3_sitelib}/%{_name}_caja-*

%files -n nemo-extension-%{name}
%license COPYING.GPL3
%{_datadir}/nemo-python/
%{python3_sitelib}/%{_name}_nemo-*

%files common
%license COPYING.GPL3
%{python3_sitelib}/%{_name}_common-*
%{_datadir}/icons/hicolor/*/*/

%files common-lang -f %{name}-common.lang

%changelog
