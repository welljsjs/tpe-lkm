
%define debug_package %{nil}
%define kernel_version %(uname -r | cut -d - -f 1)

Summary: Trusted Path Execution (TPE) Linux Kernel Module
Name: tpe
Version: 1.0
Release: 1%{?dist}
Packager: Corey Henderson <corman@cormander.com>
URL: https://github.com/cormander/tpe-lkm
Source0: %{name}-%{version}.tar.gz
License: GPLv2
Group: System Environment/Kernel
BuildRoot: %{_tmppath}/%{name}-root
Requires: kernel = %{kernel_version}

%description
Trusted Path Execution is a security feature that denies users from executing
programs that are not owned by root, or are writable. This closes the door on a
whole category of exploits where a malicious user tries to execute his or her
own code to hack the system.

%prep
%setup -q

%build

make

%install
rm -rf $RPM_BUILD_ROOT

# Create directories

mkdir -p $RPM_BUILD_ROOT/etc/{modprobe.d,sysconfig/modules}

make DESTDIR=$RPM_BUILD_ROOT install_files

%check

%post
[ -x /sbin/modprobe ] && /sbin/modprobe tpe || :

%preun
[ -x /sbin/rmmod ] && /sbin/rmmod tpe 2> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
/etc/sysconfig/modules/tpe.modules
/etc/modprobe.d/tpe.conf
/lib/modules/generic/tpe.ko
/lib/modules/generic/modules.dep

%changelog
* Wed Jul  7 2011 Corey Henderson <corman@cormander.com>
- Initial build.

