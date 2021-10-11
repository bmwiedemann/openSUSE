#
# spec file for package qml-autoreqprov
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


Name:           qml-autoreqprov
Version:        1.1
Release:        0
Summary:        Automatic dependency generator for QML files and modules
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            http://www.opensuse.org
Source0:        LICENSE
Source1:        qml.attr
Source2:        qml.req
Source3:        qmldir.attr
Source4:        qmldirreqprov.sh
Source5:        README
Requires:       jq
Requires:       rpm
BuildArch:      noarch
Requires:       (libqt5-qtdeclarative-tools if libQtQuick5)
Requires:       (qmlpluginexports-qt5 if libqt5-qtdeclarative-devel)
Requires:       (qmlpluginexports-qt6 if qt6-qml-devel)
Requires:       (qt6-declarative-tools if libQt6Qml6)
# Version 1.1 is not compatible with qt6-declarative < 6.2
Conflicts:      qt6-declarative-tools < 6.2.0

%description
Automatic dependency generator for QML files and modules.
If installed, rpm uses this to generate Requires of .qml files
and Provides of QML modules.

%prep
cp %{SOURCE0} .
cp %{SOURCE5} .

%build

%install
install -D -m 644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/fileattrs/qml.attr
install -D -m 755 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/qml.req
install -D -m 644 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/fileattrs/qmldir.attr
install -D -m 755 %{SOURCE4} %{buildroot}%{_rpmconfigdir}/qmldirreqprov.sh

%files
%license LICENSE
%doc README
%{_rpmconfigdir}/fileattrs/qml.attr
%{_rpmconfigdir}/fileattrs/qmldir.attr
%{_rpmconfigdir}/qml.req
%{_rpmconfigdir}/qmldirreqprov.sh

%changelog
