<?php

$kadi = $_POST['kadi'];
$sifre = $_POST['sifre'];

if($kadi == 'said' && $sifre == '1234')
{
	 echo "<center>Basariyla giris yapildi.</center>";
}

else
{
	  echo "<center>Yanlis</center>";
}

