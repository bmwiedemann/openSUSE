#
# spec file for package kvm_stat
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


Name:           kvm_stat
%define version %(rpm -q --qf '%%{VERSION}' kernel-source)
Version:        %{version}
Release:        0
Summary:        Monitoring Tool for KVM guests
License:        GPL-2.0-only
Group:          System/Monitoring
Url:            http://www.kernel.org/
BuildArch:      noarch
BuildRequires:  asciidoc
BuildRequires:  kernel-source >= 4.7.0
BuildRequires:  libxslt-tools

Requires:       python3-curses

Recommends:     kernel >= 4.7.0
Conflicts:      qemu < 2.6.90
Conflicts:      qemu-kvm < 2.6.90
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Patch0:         0001-tools-kvm_stat-fix-event-counts-display-for-interrup.patch
Patch1:         0002-tools-kvm_stat-fix-undue-use-of-initial-sleeptime.patch
Patch2:         0003-tools-kvm_stat-remove-unnecessary-header-redraws.patch
Patch3:         0004-tools-kvm_stat-simplify-line-print-logic.patch
Patch4:         0005-tools-kvm_stat-remove-extra-statement.patch
Patch5:         0006-tools-kvm_stat-simplify-initializers.patch
Patch6:         0007-tools-kvm_stat-move-functions-to-corresponding-class.patch
Patch7:         0008-tools-kvm_stat-show-cursor-in-selection-screens.patch
Patch8:         0009-tools-kvm_stat-display-message-indicating-lack-of-ev.patch
Patch9:         0010-tools-kvm_stat-make-heading-look-a-bit-more-like-top.patch
Patch10:        0011-tools-kvm_stat-rename-Current-column-to-CurAvg-s.patch
Patch11:        0012-tools-kvm_stat-add-new-interactive-command-h.patch
Patch12:        0013-tools-kvm_stat-add-new-interactive-command-s.patch
Patch13:        0014-tools-kvm_stat-add-new-interactive-command-o.patch
Patch14:        0015-tools-kvm_stat-display-guest-list-in-pid-guest-selec.patch
Patch15:        0016-tools-kvm_stat-fix-error-on-interactive-command-g.patch
Patch16:        0017-tools-kvm_stat-add-new-command-line-switch-i.patch
Patch17:        0018-tools-kvm_stat-add-new-interactive-command-b.patch
Patch18:        0019-tools-kvm_stat-add-f-help-to-get-the-available-event.patch
Patch19:        0020-tools-kvm_stat-Add-Python-3-support-to-kvm_stat.patch
Patch20:        0021-tools-kvm_stat-fix-command-line-option-g.patch
Patch21:        0022-tools-kvm_stat-fix-drilldown-in-events-by-guests-mod.patch
Patch22:        0023-tools-kvm_stat-fix-missing-field-update-after-filter.patch
Patch23:        0024-tools-kvm_stat-fix-extra-handling-of-help-with-field.patch
Patch24:        0025-tools-kvm_stat-add-hint-on-f-help-to-man-page.patch
Patch25:        0026-tools-kvm_stat-fix-child-trace-events-accounting.patch
Patch26:        0027-tools-kvm_stat-handle-invalid-regular-expressions.patch
Patch27:        0028-tools-kvm_stat-suppress-usage-information-on-command.patch
Patch28:        0029-tools-kvm_stat-stop-ignoring-unhandled-arguments.patch
Patch29:        0030-tools-kvm_stat-add-line-for-totals.patch
Patch30:        0031-tools-kvm_stat-sort-f-help-output.patch
Patch31:        0032-tools-kvm_stat-simplify-the-sortkey-function.patch
Patch32:        0033-tools-kvm_stat-use-a-namedtuple-for-storing-the-valu.patch
Patch33:        0034-tools-kvm_stat-use-a-more-pythonic-way-to-iterate-ov.patch
Patch34:        0035-tools-kvm_stat-avoid-is-for-equality-checks.patch
Patch35:        0036-tools-kvm_stat-fix-crash-when-filtering-out-all-non-.patch
Patch36:        0037-tools-kvm_stat-print-error-on-invalid-regex.patch
Patch37:        0038-tools-kvm_stat-fix-debugfs-handling.patch
Patch38:        0039-tools-kvm_stat-mark-private-methods-as-such.patch
Patch39:        0040-tools-kvm_stat-eliminate-extra-guest-pid-selection-d.patch
Patch40:        0041-tools-kvm_stat-separate-drilldown-and-fields-filteri.patch
Patch41:        0042-tools-kvm_stat-group-child-events-indented-after-par.patch
Patch42:        0043-tools-kvm_stat-print-Total-line-for-multiple-events-.patch
Patch43:        0044-tools-kvm_stat-Don-t-use-deprecated-file.patch
Patch44:        0045-tools-kvm_stat-fix-python3-issues.patch
Patch45:        0046-tools-kvm_stat-apply-python-2to3-fixes-to-kvm_stat.patch
Patch46:        0047-tools-kvm_stat-apply-python-2to3-fixes-to-kvm_stat2.patch
Patch47:        0048-tools-kvm_stat-apply-python-2to3-fixes-to-kvm_stat3.patch
Patch48:        0049-tools-kvm_stat-switch-python-reference-to-be-explici.patch
Patch49:        0050-tools-kvm_stat-switch-python-reference-again.patch

%description
This package provides a userspace tool "kvm_stat", which displays KVM vm exit
information as a means of monitoring vm behavior. The data is taken from the
KVM debugfs files or the vm tracepoints and outputs them as a curses ui or
simple text.

%prep
# copy necessary files from kernel-source
(tar -C /usr/src/linux -c COPYING tools scripts) | tar -x

%define SLE15_SP1_OR_LEAP15_1 0%{?sle_version} == 150100
%define FACTORY     (0%{?is_opensuse} && 0%{?suse_version} > 1500)
%define SLE_LEAP_15 (0%{?sle_version} <= 150000 && 0%{?suse_version} <= 1500)
%define SLE_LEAP_15_2 (0%{?sle_version} == 150200 && 0%{?suse_version} <= 1500)
# Only apply the first few patches to SLES15-SP1 and Leap 15.1
%if %{SLE15_SP1_OR_LEAP15_1}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%endif

# If the build is SLE15 / Leap 15 or older
%if %{SLE_LEAP_15}
%patch46 -p1
%endif

# If the build is Factory or Tumbleweed or SLE15SP2 / Leap 15.2
%if %{FACTORY} || %{SLE_LEAP_15_2}
%patch47 -p1
%patch49 -p1
%else
%patch48 -p1
%endif

%build
make -C tools/kvm/kvm_stat %{?_smp_mflags}

%install
make -C tools kvm_stat_install INSTALL_ROOT=%{buildroot}

%files
%defattr(-, root, root)
%license COPYING
%{_bindir}/kvm_stat
%{_mandir}/man1/kvm_stat*

%changelog
