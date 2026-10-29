# Troubleshooting Hadoop

Utilizar esta guía únicamente si hay problemas con Hadoop.

---

## 1. No encuentra bashrc

- Nos movemos al home en el terminal

```bash
cd ~
```

- Listamos los archivos que hay, aquí debería aparecer `.bashrc`
```bash
ls -la
```

- Si aparece, abrelo con una forma mas robusta independientemente de donde te encuentres

```bash
nano ~/.bashrc
```

- Si dice que ``nano`` no existe, entonces ejecuta la instalación

```bash
sudo apt install nano -y
```

y vuelve a intentar

```bash
nano ~/.bashrc
```

