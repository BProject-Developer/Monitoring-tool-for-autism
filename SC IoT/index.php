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
    <title>Dashboard</title> 
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
                    <a href="index.php" class="active"><span class="las la-igloo"></span> 
                    <span>Dashboard</span></a> 
                </li> 

                <?php 
                if ($_SESSION['level'] == 'dokter' OR $_SESSION['level'] == 'wali' OR $_SESSION['level'] == 'pengasuh') { 
                ?> 
                <li> 
                    <a href="datapasien.php"><span class="las la-clipboard-list"></span> 
                    <span>Data Pasien</span></a> 
                </li> 
                <?php } ?> 

                <?php 
                if ($_SESSION['level'] == 'pengasuh') { 
                ?> 
                <li> 
                    <a href="walibaru.php"><span class = "las la-clipboard-list"></span> 
                    <span>Anggota Baru</span> 
                </li> 
                <?php } ?> 

                <?php 
                if ($_SESSION['level'] == 'admin') { 
                ?> 
                <li> 
                    <a href="member.php"><span class="las la-clipboard-list"></span> 
                    <span>List Pengurus</span></a> 
                </li> 
                <li> 
                    <a href="memberbaru.php"><span class = "las la-clipboard-list"></span> 
                    <span>Member Baru</span></a> 
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
                Dashboard 
            </h2> 

            <div class="user-wrapper"> 
                <img src="senyum.png" width="40px" height="40px" alt=""> 
                <div> 
                    <h4> <?php echo $_SESSION['username']; ?> </h4> 
                    <small> <?php echo $_SESSION['level']; ?> </small> 
                </div> 
            </div> 
        </header> 
    </div> 
</body> 
</html>