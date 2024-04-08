#
# spec file for package viddy
#
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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

%global import_path github.com/sachaos/viddy/

Name:           viddy
Version:        0.4.0
Release:        0
Summary:        A modern watch command
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/sachaos/viddy
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go
BuildRequires:  golang-packaging
%{go_provides}

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
%{goprep} %import_path
%{gobuild} -mod=vendor .

%install
%{goinstall}

%check
%{gotest} %import_path

%files
%license LICENSE
%doc README.md
%{_bindir}/viddy

%changelog
