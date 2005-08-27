# $Rev: 3355 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	luit application
Summary(pl):	Aplikacja luit
Name:		xorg-app-luit
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/luit-%{version}.tar.bz2
# Source0-md5:	bd78d37a350a34ff9a52c8308970e902
Patch0:		luit-man.patch
Patch1:		luit-freebsd.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libfontenc-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/luit-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
luit application.

%description -l pl
Aplikacja luit.


%prep
%setup -q -n luit-%{version}
%patch0 -p1
%patch1 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
