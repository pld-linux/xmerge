Summary:	Image merging tool
Summary(pl.UTF-8):  Narzędzie do łączenia obrazów
Name:		xmerge
Version:	0.1.1
Release:	0.1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	ffb929265d041f103b7d629d80ab184b
URL:		http://xmerge.sourceforge.net
Requires:   xorg-lib-libX11
BuildRequires:  xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xmerge is an open source program for merging and correcting rotated, skewed
or generally linearly distorted images, featuring a X gui.

%description -l pl.UTF-8
xmerge jest narzędziem przeznaczonym do łączenia i korygowania obróconych,
przechylonych i w inny sposób zniekształconych liniowo obrazów. Posiada
interfejs graficzny.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
install -d $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%doc README
