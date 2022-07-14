
function crearCertificado(values){
    try {
        // jsPdf
        window.jsPDF = window.jspdf.jsPDF;
        const doc = new jsPDF({
          orientation: 'p',
          unit: 'mm',
          format: 'a4'
        });

        const margins = {
          top: 58,
          left: 32,
          right: 32,
          bottom: 0
        };
        
        
        doc.rect(margins.left + 4, margins.top, 25, 30, 'S');

        doc.addFileToVFS('Avantgarde.ttf', fontsB64.avantgarde.normal);
        doc.addFont('Avantgarde.ttf', 'avantgarde', 'normal');
        doc.addFileToVFS('Avantgarde-b.ttf', fontsB64.avantgarde.bold);
        doc.addFont('Avantgarde-b.ttf', 'avantgarde', 'bold');
        doc.addFileToVFS('Avantgarde-i.ttf', fontsB64.avantgarde.italic);
        doc.addFont('Avantgarde-i.ttf', 'avantgarde', 'italic');

        doc.addFileToVFS('Arial.ttf', fontsB64.arial.normal);
        doc.addFont('Arial.ttf', 'arial', 'normal');
        doc.addFileToVFS('Arial-b.ttf', fontsB64.arial.bold);
        doc.addFont('Arial-b.ttf', 'arial', 'bold');
        
        doc.setFontSize(14);
        doc.setFont('avantgarde', 'bold');
        doc.text(margins.left + 60, 3 + margins.top, 'CERTIFICADO DE ESTUDIOS');
        doc.setFontSize(9);
        doc.setFont('avantgarde', 'normal');
        const textInit = `La Universidad Tecnológica certifica que según constancias existentes en el archivo escolar, el C. ${values.nombre} ${values.apellidoP} ${values.apellidoM} con matrícula ${values.matricula} cursó y aprobó las asignaturas que integran el plan de estudios ${values.planE} en el periodo escolar ${values.periodoInit} - ${values.periodoEnd} de la carrera de ${values.tipoC} en ${values.nombreC} Area ${values.areaC} obteniendo las calificaciones finales que a continuación se anotan:`
        doc.text(textInit, margins.left + 40, 8 + margins.top,{ maxWidth: 105, align: "justify"});
        doc.setLineWidth(0.5);
        doc.line(margins.left, margins.top + 35, margins.left + 146, margins.top + 35, 'FD');
        doc.setLineWidth(0.3);
        
        // tabla de calificaciones
        doc.line(margins.left, margins.top + 40, margins.left + 146, margins.top + 40, 'FD'); // - 1
        doc.line(margins.left, margins.top + 40, margins.left, margins.top + 50, 'FD'); // | 1
        doc.line(margins.left + 110, margins.top + 40, margins.left + 110, margins.top + 50, 'FD'); // | 2
        doc.line(margins.left + 122, margins.top + 40, margins.left + 122, margins.top + 50, 'FD'); // | 3
        doc.line(margins.left + 122, margins.top + 44, margins.left + 146, margins.top + 44, 'FD'); // - 2
        doc.line(margins.left + 134, margins.top + 44, margins.left + 134, margins.top + 50, 'FD'); // | 4
        doc.line(margins.left + 146, margins.top + 40, margins.left + 146, margins.top + 50, 'FD'); // | 5
        doc.line(margins.left, margins.top + 50, margins.left + 146, margins.top + 50, 'FD'); // - 3
        doc.setFontSize(7);
        doc.setFont('avantgarde', 'bold');
        doc.text(margins.left + 46, margins.top + 45, 'ASIGNATURAS'); // T 1
        doc.text(margins.left + 112.2, margins.top + 45, 'HORAS'); // T 2
        doc.text(margins.left + 126.5, margins.top + 42.5, 'CALIFICACIÓN'); // T 3
        doc.text(margins.left + 123.3, margins.top + 47.5, 'NUMERO'); // T 4
        doc.text(margins.left + 139.9, margins.top + 46.8, 'CALIFICACIÓN', {align: 'center', maxWidth: 11}); // T 5
        
        // 52 asignaturas
        // const calificacionesM = [
        //   {
        //     'asignatura': 'Matemáticas',
        //     'horas': '50',
        //     'calificacion': 'AU',
        //     'numero': '10'
        //   },{
        //     'asignatura': 'Lenguaje',
        //     'horas': '75',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Ciencias',
        //     'horas': '35',
        //     'calificacion': 'SA',
        //     'numero': '8'
        //   },
        //   {
        //     'asignatura': 'Historia',
        //     'horas': '91',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Geografía',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Arte',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Educación Física',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Inglés',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Religión',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Tecnología',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Cultura',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Deportes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Artes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Educación',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Deportes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Artes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Educación',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Deportes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Artes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Educación',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Deportes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Artes',
        //     'horas': '50',
        //     'calificacion': 'AU',
        //     'numero': '10'
        //   },
        //   {
        //     'asignatura': 'Educación',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Deportes',
        //     'horas': '50',
        //     'calificacion': 'SA',
        //     'numero': '8'
        //   },
        //   {
        //     'asignatura': 'Artes',
        //     'horas': '446',
        //     'calificacion': 'SA',
        //     'numero': '8'
        //   },
        //   {
        //     'asignatura': 'Educación',
        //     'horas': '50',
        //     'calificacion': 'SA',
        //     'numero': '8'
        //   },
        //   {
        //     'asignatura': 'Matemáticas',
        //     'horas': '50',
        //     'calificacion': 'AU',
        //     'numero': '10'
        //   },{
        //     'asignatura': 'Lenguaje',
        //     'horas': '75',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Ciencias',
        //     'horas': '35',
        //     'calificacion': 'SA',
        //     'numero': '8'
        //   },
        //   {
        //     'asignatura': 'Historia',
        //     'horas': '91',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Geografía',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Arte',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Educación Física',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Inglés',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Religión',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Tecnología',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Cultura',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Deportes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Artes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Educación',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Deportes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Artes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Educación',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Deportes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Artes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Educación',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Deportes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Artes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Educación',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Deportes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Artes',
        //     'horas': '50',
        //     'calificacion': 'DE',
        //     'numero': '9'
        //   },
        //   {
        //     'asignatura': 'Educación',
        //     'horas': '50',
        //     'calificacion': 'SA',
        //     'numero': '8'
        //   },
        // ];

        var countCalificacion = 0;
        var countMateria = 0;
        var alturaNew = 0;
        var cabeEnHoja1 = true;
        if (typeof values.calificaciones == 'string') {
          values.calificaciones = JSON.parse(values.calificaciones);
        }

        values.calificaciones.forEach((asig,i) =>{
          if (i < 50){
            doc.setFont('avantgarde', 'normal');
            doc.line(margins.left, margins.top + 50 + (i*3), margins.left, margins.top + 53 + (i*3), 'FD'); // | 1
            doc.line(margins.left, margins.top + 53 + (i*3), margins.left + 146, margins.top + 53 + (i*3), 'FD') // - 2
            doc.line(margins.left + 110, margins.top + 50 + (i*3), margins.left + 110, margins.top + 53 + (i*3), 'FD'); // | 3
            doc.line(margins.left + 122, margins.top + 50 + (i*3), margins.left + 122, margins.top + 53 + (i*3), 'FD'); // | 4
            doc.line(margins.left + 134, margins.top + 50 + (i*3), margins.left + 134, margins.top + 53 + (i*3), 'FD'); // | 5
            doc.line(margins.left + 146, margins.top + 50 + (i*3), margins.left + 146, margins.top + 53 + (i*3), 'FD'); // | 6
            doc.setFontSize(8);
            doc.text(asig.materia, margins.left + 5, margins.top + 52.4 + (i*3), { align: 'left' }); // T 1
            doc.setFontSize(7);
            doc.text(asig.horas.toString(), margins.left + 116, margins.top + 52.4 + (i*3), { align: 'center' }); // T 2
            doc.text(asig.calificacion.toString(), margins.left + 128, margins.top + 52.4 + (i*3), { align: 'center' }); // T 4
            
            switch (asig.calificacion) {
              case 10:
                asig.calificacionStr = 'AU'
                break;
              case 9:
                asig.calificacionStr = 'DE'
                break;
              case 8:
                asig.calificacionStr = 'SA'
                break;
              default:
                asig.calificacionStr = 'NA'
                break;
            }

            doc.text(asig.calificacionStr, margins.left + 138.3, margins.top + 52.4 + (i*3), { align: 'left' }); // T 3
            
            countCalificacion += parseInt(asig.calificacion);
            countMateria = i + 1;
            alturaNew = margins.top + 53 + (i*3);
            
          }else{
            cabeEnHoja1 = false;
          }
        })
        //altura actual  = alturaNew;

        if (cabeEnHoja1) {
          doc.line(margins.left, alturaNew, margins.left, alturaNew + 3, 'FD'); // | 1
          doc.line(margins.left, alturaNew + 3, margins.left + 146, alturaNew + 3, 'FD') // - 2
          doc.line(margins.left + 122, alturaNew, margins.left + 122, alturaNew + 3, 'FD'); // | 3
          doc.line(margins.left + 146, alturaNew, margins.left + 146, alturaNew + 3, 'FD'); // | 4
          doc.setFont('avantgarde', 'bold');
          doc.text(margins.left + 48, alturaNew + 2.3, 'Promedio Final'); 
          doc.setFont('avantgarde', 'normal');
          doc.text(margins.left + 132.5, alturaNew + 2.3, (countCalificacion/countMateria).toFixed(1).toString()); 
        }
        
        
        doc.addPage();

        if (cabeEnHoja1 == false) {

          values.calificaciones.slice(50).forEach((asig,i) =>{

            doc.setFont('avantgarde', 'normal');
            doc.line(margins.left, margins.top + 0 + (i*3), margins.left + 146, margins.top + 0 + (i*3), 'FD') // - 0
            doc.line(margins.left, margins.top + 0 + (i*3), margins.left, margins.top + 3 + (i*3), 'FD'); // | 1
            doc.line(margins.left, margins.top + 3 + (i*3), margins.left + 146, margins.top + 3 + (i*3), 'FD') // - 2
            doc.line(margins.left + 110, margins.top + 0 + (i*3), margins.left + 110, margins.top + 3 + (i*3), 'FD'); // | 3
            doc.line(margins.left + 122, margins.top + 0 + (i*3), margins.left + 122, margins.top + 3 + (i*3), 'FD'); // | 4
            doc.line(margins.left + 134, margins.top + 0 + (i*3), margins.left + 134, margins.top + 3 + (i*3), 'FD'); // | 5
            doc.line(margins.left + 146, margins.top + 0 + (i*3), margins.left + 146, margins.top + 3 + (i*3), 'FD'); // | 6
            doc.setFontSize(8);
            doc.text(asig.materia, margins.left + 5, margins.top + 2.4 + (i*3), { align: 'left' }); // T 1
            doc.setFontSize(7);
            doc.text(asig.horas.toString(), margins.left + 116, margins.top + 2.4 + (i*3), { align: 'center' }); // T 2
            doc.text(asig.calificacion.toString(), margins.left + 128, margins.top + 2.4 + (i*3), { align: 'center' }); // T 4
            
            switch (asig.calificacion) {
              case 10:
                asig.calificacionStr = 'AU'
                break;
              case 9:
                asig.calificacionStr = 'DE'
                break;
              case 8:
                asig.calificacionStr = 'SA'
                break;
              default:
                asig.calificacionStr = 'NA'
                break;
            }

            doc.text(asig.calificacionStr, margins.left + 138.3, margins.top + 2.4 + (i*3), { align: 'left' }); // T 3
            
            countCalificacion += parseInt(asig.calificacion);
            countMateria +=  1;
            alturaNew = margins.top + 3 + (i*3);
            
          })

          doc.line(margins.left, alturaNew, margins.left, alturaNew + 3, 'FD'); // | 1
          doc.line(margins.left, alturaNew + 3, margins.left + 146, alturaNew + 3, 'FD') // - 2
          doc.line(margins.left + 122, alturaNew, margins.left + 122, alturaNew + 3, 'FD'); // | 3
          doc.line(margins.left + 146, alturaNew, margins.left + 146, alturaNew + 3, 'FD'); // | 4
          doc.setFont('avantgarde', 'bold');
          doc.text(margins.left + 48, alturaNew + 2.3, 'Promedio Final'); 
          doc.setFont('avantgarde', 'normal');
          doc.text(margins.left + 132.5, alturaNew + 2.3, (countCalificacion/countMateria).toFixed(1).toString()); 
        
          margins.top = alturaNew + 3 + 10;
        }




        //competencias
        const competenciasEspecificas = [
          {
            'competencia': 'lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. ',
          },
          {
            'competencia': 'lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. ',
          },
          {
            'competencia': 'lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem.',
          },
        ]
        const competenciasGenericas = [
          {
            'competencia': 'lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. ',
          },
          {
            'competencia': 'lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem. ',
          },
          {
            'competencia': 'lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem.',
          },
          {
            'competencia': 'lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quidem.',
          },
        ]

        let countCompetencias = 0;
        let competenciasESentencia = ''
        let alturaESentencia = 0;
        competenciasEspecificas.forEach((comp) =>{
          competenciasESentencia += comp.competencia + '\n'+ '\n'
          comp.competencia.length > 117 
          ? alturaESentencia += parseInt(Math.ceil(comp.competencia.length/115))
          : alturaESentencia += 2
          countCompetencias += 1;
        })

        let competenciasGSentencia = ''
        let alturaGSentencia = 0;
        competenciasGenericas.forEach((comp) =>{
          competenciasGSentencia += comp.competencia + '\n'+ '\n'
          comp.competencia.length > 117
          ? alturaGSentencia += parseInt(Math.ceil(comp.competencia.length/115))
          : alturaGSentencia += 2
          countCompetencias += 1;
        })


        doc.line(margins.left, margins.top, margins.left, margins.top + 6, 'FD'); // | 1
        doc.line(margins.left, margins.top, margins.left + 146, margins.top, 'FD'); // - 2
        doc.line(margins.left + 146, margins.top, margins.left + 146, margins.top + 6, 'FD'); // | 3
        doc.line(margins.left, margins.top + 3, margins.left + 146, margins.top + 3, 'FD'); // - 4
        doc.line(margins.left, margins.top + 6, margins.left + 146, margins.top + 6, 'FD'); // - 5

        doc.setFontSize(8);
        doc.setFont('arial', 'bold');
        doc.text(margins.left + 21, margins.top + 2.5, 'COMPETENCIAS PROFESIONALES QUE AVALA EL PRESIDENTE CERTIFICADO');
        doc.text(margins.left + 5, margins.top + 5.4, 'Competencias Especificas ');

        doc.setFont('arial', 'normal');
        doc.text(competenciasESentencia, margins.left + 5, margins.top + 9 , { align: 'justify', maxWidth: 140 });
        
        doc.line(margins.left, margins.top + 6, margins.left, margins.top + (alturaESentencia * 5), 'FD'); // | 1
        doc.line(margins.left + 146, margins.top + 6, margins.left + 146, margins.top + (alturaESentencia * 5), 'FD'); // | 2

        alturaNew = margins.top + (alturaESentencia * 5);
        doc.line(margins.left, alturaNew, margins.left + 146, alturaNew, 'FD'); // - 1
        doc.line(margins.left, alturaNew, margins.left, alturaNew + 3, 'FD'); // | 2
        doc.line(margins.left + 146, alturaNew, margins.left + 146, alturaNew + 3, 'FD'); // | 2
        doc.line(margins.left, alturaNew + 3, margins.left + 146, alturaNew + 3, 'FD'); // - 4

        doc.setFont('arial', 'bold');
        doc.text(margins.left + 5, alturaNew + 2.4, 'Competencias Genéricas');

        doc.setFont('arial', 'normal');
        doc.text(competenciasGSentencia, margins.left + 5, alturaNew + 6 , { align: 'justify', maxWidth: 140 });
        
        doc.line(margins.left, alturaNew + 3, margins.left, alturaNew + (alturaGSentencia * 5), 'FD'); // | 1
        doc.line(margins.left + 146, alturaNew + 3, margins.left + 146, alturaNew + (alturaGSentencia * 5), 'FD'); // | 2
        
        alturaNew = alturaNew + (alturaGSentencia * 5);
        doc.line(margins.left, alturaNew, margins.left + 146, alturaNew, 'FD'); // - 3


        let dia, mes, anio;
        new Date().getDate().toString().length == 1 ? dia = '0' + new Date().getDate().toString() : dia = new Date().getDate().toString();
        const meses = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'];
        mes = meses[new Date().getMonth()]
        anio = new Date().getFullYear().toString();
        switch (countCompetencias.toString().length) {
          case 1:
            countCompetencias = Unidades(countCompetencias).toLocaleLowerCase();
            break;
          case 2:
            countCompetencias = Decenas(countCompetencias).toLocaleLowerCase();
            break;
          case 3:
            countCompetencias = Centenas(countCompetencias).toLocaleLowerCase();
        
          default:
            break;
        }
        const text1 = `El presente certificado ampara ${countMateria} asignaturas de un total de ${countMateria} y ${countCompetencias} competencias profesionales de un total de ${countCompetencias}.`
        const text2 = `Expedido en El Carmen Xalpatlahuaya de Huamantla, Tlaxcala., a los ${dia} dias del mes de ${mes} del año ${anio}`

        const alturaText1 = parseInt(Math.ceil(text1.length/115)) * 4;
        const alturaText2 = parseInt(Math.ceil(text2.length/115)) * 7;

        doc.setFontSize(8);
        doc.setFont('avantgarde', 'normal');
        doc.text(margins.left + 5, alturaNew + alturaText1 , text1, { align: 'left', maxWidth: 140 });
        doc.text(margins.left + 5, alturaNew + alturaText1 + alturaText2 + 3, text2, { align: 'left', maxWidth: 140 });

        alturaNew = alturaNew + alturaText1 + alturaText2 + 3;

        //firmas
        doc.line(margins.left, alturaNew + 20, margins.left + 65, alturaNew + 20, 'FD'); // - 1
        doc.line(margins.left + 85, alturaNew + 20, margins.left + 146, alturaNew + 20, 'FD'); // - 2

        doc.text(margins.left + 32.5, alturaNew + 24, 'Arq. Alfredo Ajuria Huerta', { align: 'center', maxWidth: 55 });
        doc.text(margins.left + 117.5, alturaNew + 24, 'M. en C. Yesenia Ricón Enríquez', { align: 'center', maxWidth: 135 });

        doc.text(margins.left + 32.5, alturaNew + 29, 'Jefe del Departamento de Servicios Escolares', { align: 'center', maxWidth: 55 });
        doc.text(margins.left + 117.5, alturaNew + 29, `Directora de la Carrera de ${values.carrera_titulacion} Area ${values.area_carrera_titulacion}`, { align: 'center', maxWidth: 135 });
        

        //Ultima tabla
        const newMargins = {
          left: margins.left - 10,
          right: margins.left + 146 + 10,
        }
        doc.line(newMargins.left, alturaNew + 50, newMargins.right, alturaNew + 50, 'FD'); // - 1
        doc.line(newMargins.left, alturaNew + 50, newMargins.left, alturaNew + 50 + 10, 'FD'); // | 2
        doc.line(newMargins.right, alturaNew + 50, newMargins.right, alturaNew + 50 + 10, 'FD'); // | 3
        doc.line(newMargins.left, alturaNew + 54, newMargins.right, alturaNew + 54, 'FD'); // - 4
        doc.line(newMargins.left, alturaNew + 57, newMargins.right, alturaNew + 57, 'FD'); // - 5
        doc.line(newMargins.left, alturaNew + 60, newMargins.right, alturaNew + 60, 'FD'); // - 6

        doc.line(newMargins.left + 30, alturaNew + 54, newMargins.left + 30, alturaNew + 60, 'FD'); // | 7
        doc.line(newMargins.left + 60, alturaNew + 54, newMargins.left + 60, alturaNew + 60, 'FD'); // | 8
        doc.line(newMargins.left + 68, alturaNew + 54, newMargins.left + 68, alturaNew + 60, 'FD'); // | 9
        doc.line(newMargins.left + 98, alturaNew + 54, newMargins.left + 98, alturaNew + 60, 'FD'); // | 10
        doc.line(newMargins.left + 102, alturaNew + 54, newMargins.left + 102, alturaNew + 60, 'FD'); // | 11
        doc.line(newMargins.left + 132, alturaNew + 54, newMargins.left + 132, alturaNew + 60, 'FD'); // | 12
        doc.line(newMargins.left + 136, alturaNew + 54, newMargins.left + 136, alturaNew + 60, 'FD'); // | 13
        
        doc.setFontSize(5);
        doc.setFont('arial', 'bold');
        doc.text(newMargins.left + 75, alturaNew + 53, 'DESCRIPCIÓN DE LA ESCALA ALFANUMÉRICA', { align: 'center', maxWidth: newMargins.right }); // T 1

        doc.setFont('arial', 'normal');
        doc.text(newMargins.left + 2, alturaNew + 56.5, 'Asignaturas No integradoras', { align: 'left' }); // T 2
        doc.text(newMargins.left + 2, alturaNew + 59.5, 'Asignaturas Integradoras', { align: 'left' }); // T 3

        doc.text(newMargins.left + 30 + 2, alturaNew + 56.5, 'AU = Autónomo', { align: 'left' }); // T 4
        doc.text(newMargins.left + 30 + 2, alturaNew + 59.5, 'CA = Competente Autónomo', { align: 'left' }); // T 5

        doc.text(newMargins.left + 60 + 3, alturaNew + 56.5, '10', { align: 'left' }); // T 6
        doc.text(newMargins.left + 60 + 3, alturaNew + 59.5, '10', { align: 'left' }); // T 7

        doc.text(newMargins.left + 68 + 2, alturaNew + 56.5, 'DE = Destacado', { align: 'left' }); // T 8
        doc.text(newMargins.left + 68 + 2, alturaNew + 59.5, 'CD = Competente Destacado', { align: 'left' }); // T 9

        doc.text(newMargins.left + 98 + 1.5, alturaNew + 56.5, '9', { align: 'left' }); // T 10
        doc.text(newMargins.left + 98 + 1.5, alturaNew + 59.5, '9', { align: 'left' }); // T 11

        doc.text(newMargins.left + 102 + 2, alturaNew + 56.5, 'SA = Satisfactorio', { align: 'left' }); // T 12
        doc.text(newMargins.left + 102 + 2, alturaNew + 59.5, 'CO = Competente', { align: 'left' }); // T 13

        doc.text(newMargins.left + 132 + 1.5, alturaNew + 56.5, '8', { align: 'left' }); // T 14
        doc.text(newMargins.left + 132 + 1.5, alturaNew + 59.5, '8', { align: 'left' }); // T 15

        doc.text(newMargins.left + 136 + 2, alturaNew + 56.5, 'NA = No Acreditado', { align: 'left' }); // T 16
        doc.text(newMargins.left + 136 + 2, alturaNew + 59.5, 'NA = No Acreditado', { align: 'left' }); // T 17



        doc.save(values.matricula+'_'+new Date().getTime()+'_CT.pdf');
    } catch (error) {
    console.log(error);
    }
}