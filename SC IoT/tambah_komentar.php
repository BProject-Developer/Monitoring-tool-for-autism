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
    <title>Tambah Komentar</title> 
    <link rel="stylesheet" href="style.css?d=<?php echo time(); ?>" /> 
</head> 
<body> 
    <div class="main-content"> 
        <header> 
            <h2>Tambah Komentar</h2> 
        </header> 

        <main> 
            <div class="card"> 
                <div class="card-body"> 
                    <?php 
                    $id = $_GET['id']; 
                    $sql = "SELECT * FROM data WHERE id = '$id'"; 
                    $query = mysqli_query($conn, $sql); 
                    $row = mysqli_fetch_assoc($query); 
                    ?> 

                    <form action="" method="POST"> 
                        <label>Nama Pasien:</label> 
                        <input type="text" name="username" value="<?php echo $row['username']?>" readonly> 

                        <label>Komentar:</label> 
                        <textarea name="komentar"></textarea> 

                        <input type="submit" name="kirim" value="Kirim"> 
                    </form> 

                    <?php 
                    if (isset($_POST['kirim'])) { 
                        $komentar = $_POST['komentar']; 
                        $sql1 = "UPDATE data SET komentar= '$komentar' WHERE id='$id'"; 
                        mysqli_query($conn, $sql1); 
                        header('Location: datapasien.php'); 
                    } 
                    ?> 
                </div> 
            </div>   
        </main> 
    </div> 
</body> 
</html>