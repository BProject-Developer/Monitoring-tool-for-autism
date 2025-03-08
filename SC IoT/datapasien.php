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
    <title>Data Pasien</title> 
    <link rel="stylesheet" href="style.css?d=<?php echo time(); ?>" /> 
</head> 
<body> 
    <input type="checkbox" id="nav-toggle"> 
    <div class="sidebar"> 
        <div class="sidebar-brand"> 
            <h2><span class="lab la-accusoft"></span> <span>Home</span></h2> 
        </div> 

        <div class="sidebar-menu"> 
            <ul> 
                <li> 
                    <a href="index.php"><span class="las la-igloo"></span> 
                    <span>Dashboard</span></a> 
                </li> 

                <?php if ($_SESSION['level'] == 'dokter' OR $_SESSION['level'] == 'wali' OR $_SESSION['level'] == 'pengasuh') { ?> 
                <li> 
                    <a href="datapasien.php" class="active"><span class="las la-clipboard-list"></span> 
                    <span>Data Pasien</span></a> 
                </li> 
                <?php } ?> 

                <li> 
                    <a href="login.php"><span class="las la-user-circle"></span> 
                    <span>Logout</span></a> 
                </li> 
            </ul> 
        </div> 
    </div> 

    <div class="main-content"> 
        <header> 
            <h2> 
                <label for="nav-toggle"> 
                    <span class="las la-bars"></span> 
                </label> 
                Data Pasien
            </h2> 

            <div class="user-wrapper"> 
                <img src="senyum.png" width="40px" height="40px" alt=""> 
                <div> 
                    <h4><?php echo $_SESSION['username']; ?></h4> 
                    <small><?php echo $_SESSION['level']; ?></small> 
                </div> 
            </div> 
        </header> 

        <main> 
            <div class="card"> 
                <div class="card-header"> 
                    <h3>Data Pasien</h3> 
                </div> 

                <div class="card-body"> 
                    <table width="100%"> 
                        <thead> 
                            <tr> 
                                <td>Username</td> 
                                <td>Tanggal</td> 
                                <td>Ammonia</td> 
                                <td>Kondisi</td> 
                                <td>Status</td> 
                                <?php if ($_SESSION['level'] == 'dokter') { ?> 
                                <td>Edit</td> 
                                <td>Hapus</td> 
                                <?php } ?> 
                            </tr> 
                        </thead> 
                        <tbody> 
                            <?php 
                            $sql = "SELECT * FROM data ORDER BY tanggal DESC";  
                            $query = mysqli_query($conn, $sql); 
                            while ($row = mysqli_fetch_array($query)) { 
                            ?> 
                            <tr> 
                                <td><?php echo $row['username']; ?></td> 
                                <td><?php echo $row['tanggal']; ?></td> 
                                <td><?php echo $row['ammonia']; ?></td> 
                                <td><?php echo $row['classification']; ?></td> 
                                <td>
                                    <?php if ($row['komentar'] == "") { ?>
                                        <span class="status pink"></span> Belum diberi komentar 
                                    <?php } else { ?>
                                        <span class="status purple"></span> <?php echo $row['komentar']; ?> 
                                    <?php } ?>
                                </td> 
                                <?php if ($_SESSION['level'] == 'dokter') { ?> 
                                <td>
                                    <a href="tambah_komentar.php?id=<?php echo $row['id']; ?>">
                                        <span class="las la-folder-plus"></span> 
                                    </a> 
                                </td> 
                                <td> 
                                    <a href="hapus_komentar.php?id=<?php echo $row['id']; ?>">
                                        <span class="las la-folder-minus"></span>
                                    </a> 
                                </td>     
                                <?php } ?> 
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