<?php 
session_start(); 
include 'koneksi.php'; 
clearstatcache(); 
if ($_SESSION['username'] == '') { 
    header('Location: login.php'); 
} 

$id = $_GET['id']; 
$sql = "SELECT * FROM data WHERE id = '$id'"; 
$query = mysqli_query($conn, $sql); 
$row = mysqli_fetch_assoc($query); 

$komentar = ''; 
$tanggal = $row['tanggal']; 
$sql1 = "UPDATE data SET komentar= '$komentar', tanggal = '$tanggal' WHERE id='$id'"; 
$query1 = mysqli_query($conn, $sql1); 
header('Location: datapasien.php'); 
?>