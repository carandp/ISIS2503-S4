const express = require('express');
const nodemailer = require('nodemailer');

const app = express();
const port = 8080;

// Middleware to parse JSON bodies
app.use(express.json());

// Email configuration
const transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 587,
    secure: false, // true for 465, false for other ports
    auth: {
        user: 'alertasofipensiones@gmail.com', // Replace with your email
        pass: 'mngu ubja zavm uxsx' // Replace with your email password
    }
});

// Route to handle notifications
app.post('/notificaciones', async (req, res) => {
    const { id, institucion, tipo, descripcion, total, correo } = req.body;

    // Email options
    const mailOptions = {
        from: 'alertasofipensiones@gmail.com', // Replace with your email
        to: correo, // Replace with recipient email
        subject: 'Factura Generada',
        text: `Se ha tu factura:
        ID: ${id}
        Institución: ${institucion}
        Tipo: ${tipo}
        Descripción: ${descripcion}
        Total: ${total}`
    };

    // Send email
    try {
        await transporter.sendMail(mailOptions);
        res.status(200).send('Email sent successfully');
    } catch (error) {
        console.error('Error sending email:', error);
        res.status(500).send('Error sending email');
    }
});

app.listen(port, () => {
    console.log(`Notification service listening at http://localhost:${port}`);
});