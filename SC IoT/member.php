<!DOCTYPE html> 
<?php 
session_start(); 
include 'koneksi.php'; 
clearstatcache(); 
if ($_SESSION['username'] == '') { 
    header('Location: login.php'); 
} 
?> 

<html lang="en"> 
<head> 
    <meta charset="UTF-8"> 
    <title>List Pengurus</title> 
    <link rel="stylesheet" href="style.css?d=<?php echo time(); ?>" /> 
</head> 
<body> 
    <div class="main-content"> 
        <header> 
            <h2>List Pengurus</h2> 
        </header> 

        <main> 
            <div class="card"> 
                <div class="card-header"> 
                    <h3>Tabel List Pengurus</h3> 
                </div> 
                 
                <div class="card-body"> 
                    <table width="100%"> 
                        <thead> 
                            <tr> 
                                <td>Username</td>                                    
                                <td>Tanggal Daftar</td> 
                                <td>Level</td> 
                            </tr> 
                        </thead> 
                        <tbody> 
                            <?php 
                            $sql = "SELECT * FROM user WHERE level = 'dokter' OR level = 'pengasuh' ORDER BY username DESC"; 
                            $query = mysqli_query($conn, $sql); 
                            while ($row = mysqli_fetch_array($query)) { 
                            ?> 
                            <tr> 
                                <td><?php echo $row['username']; ?></td> 
                                <td><?php echo $row['tanggal_daftar']; ?></td> 
                                <td><?php echo $row['level']; ?></td> 
                            </tr> 
                            <?php } ?> 
                        </tbody> 
                    </table> 
                </div> 
            </div> 
        </main> 
    </div> 
</body> 
</html>