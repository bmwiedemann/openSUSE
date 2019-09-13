#
# spec file for package live-kiwi-hook
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


Name:           live-kiwi-hook
Version:        1.0
Release:        0
Summary:        KIWI Hook for Checking and Renaming the Live Images
License:        GPL-3.0-only
Group:          Development/Tools/Other
URL:            https://build.opensuse.org/package/show/openSUSE:Factory/live-kiwi-hook
Source1:        kiwi_post_run
Source2:        gpl-3.0.txt
BuildRequires:  coreutils
Requires:       coreutils
Requires:       sed
Requires:       util-linux
Conflicts:      kiwi_post_run
Provides:       kiwi_post_run
BuildArch:      noarch

%description
This package contains a script that is run after building the Live Images with KIWI.

%prep
%setup -q -T -c
cp %{SOURCE2} .

%build

%install
install -Dm 755 %{SOURCE1} %{buildroot}%{_prefix}/lib/build/kiwi_post_run

%files
%license gpl-3.0.txt
%dir %{_prefix}/lib/build
%{_prefix}/lib/build/kiwi_post_run

%changelog
