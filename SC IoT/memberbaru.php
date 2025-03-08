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
    <title>Tambah Pengurus Baru</title> 
    <link rel="stylesheet" href="style.css?d=<?php echo time(); ?>" /> 
</head> 
<body> 
    <div class="main-content"> 
        <header> 
            <h2>Tambah Pengurus Baru</h2> 
        </header> 

        <main> 
            <div class="card"> 
                <div class="card-header"> 
                    <h3>Isilah data calon pengurus di bawah ini</h3> 
                </div> 

                <div class="card-body"> 
                    <form name="daftarwali" method="POST" action=""> 
                        <label for="username">Masukkan username:</label> 
                        <input type="text" name="userbaru" placeholder="Masukkan username"> 

                        <label for="password">Masukkan password:</label> 
                        <input type="password" name="passbaru" placeholder="Masukkan password"> 

                        <label for="level">Pilih level:</label> 
                        <select id="level" name="level"> 
                            <option value="dokter">Dokter</option> 
                            <option value="pengasuh">Pengasuh</option> 
                        </select> 

                        <input type="submit" name="daftar" value="Daftar Sekarang"> 
                    </form> 

                    <?php 
                    if (isset($_POST['daftar'])){ 
                        $user = $_POST['userbaru'];  
                        $pass = $_POST['passbaru']; 
                        $level = $_POST['level']; 

                        $sql = "INSERT INTO user (username, password, level) VALUES ('$user', '$pass', '$level')"; 

                        if (!mysqli_query($conn, $sql)) { 
                            echo 'Not Inserted. Member telah terdaftar';  
                        } else { 
                            echo 'Inserted'; 
                        } 
                    } 
                    ?>
                </div> 
            </div> 
        </main> 
    </div> 
</body> 
</html>