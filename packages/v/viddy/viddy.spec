#
# spec file for package viddy
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2023-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           viddy
Version:        1.2.1
Release:        0
Summary:        A modern watch command
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/sachaos/viddy
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
Modern watch command.
Features:
* Basic features of original watch command:
  + Execute command periodically, and display the result.
  + color output.
  + diff highlight.
* Time machine mode:
  + Rewind like video.
  + Go to the past, and back to the future.
* See output in pager.
* Vim like keymaps.
* Search text.
* Suspend and restart execution.
* Run command in precise intervals forcibly.
* Support shell alias
* Customize keymappings.
* Customize color.

%prep
%autosetup -a 1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/viddy

%changelog
